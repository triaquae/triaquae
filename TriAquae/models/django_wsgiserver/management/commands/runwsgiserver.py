#!/usr/bin/env python
"""
Idea and code snippets borrowed from http://www.xhtml.net/scripts/Django-CherryPy-server-DjangoCerise
Adapted to run as a management command
switched to standalone
"""


import sys, os, signal, time, errno
from datetime import datetime
from pprint import (pprint, pformat)
import logging
logger = logging.getLogger('django_wsgiserver')
logger.setLevel(logging.WARNING)
logger.addHandler(logging.StreamHandler())

from socket import gethostname
from django.core.management.base import BaseCommand
import django_wsgiserver.wsgiutil
from django_wsgiserver import wsgiserver

CPWSGI_HELP = r"""
  Run this project in CherryPy's production quality http webserver.
  Note that it's called wsgiserver but it is actually a complete http server.

    runwsgiserver [options] [cpwsgi settings] [stop]

Optional CherryPy server settings: (setting=value)
  host=HOSTNAME         hostname to listen on
                        Defaults to 127.0.0.1,
                        (set to 0.0.0.0 to bind all ip4 interfaces or :: for
                        all ip6 interfaces)
  port=PORTNUM          port to listen on
                        Defaults to 8000
  server_name=STRING    CherryPy's SERVER_NAME environ entry
                        Defaults to localhost
  daemonize=BOOL        whether to detach from terminal
                        Defaults to False. This option is incompatible with autoreload
                        currently.
  pidfile=FILE          write the spawned process-id to this file
  workdir=DIRECTORY     change to this directory when daemonizing
  threads=NUMBER        Number of threads for server to use
  ssl_certificate=FILE  SSL certificate file
  ssl_private_key=FILE  SSL private key file
  server_user=STRING    user to run daemonized process
                        Defaults to www-data
  server_group=STRING   group to daemonized process
                        Defaults to www-data

  staticserve=True|False|collectstatic]
                        If True, serve the static files automatically using
                        django.contrib.staticfiles like the builting django server.
                        If staticserve=collectstatic, instead serve static files
                        from a single directory at STATIC_ROOT. You need to run
                        "manage.py collectstatic" first.
                        Defaults to True.

  adminserve=True|False  Deprecated. Has no effect. The admin is served if
                         staticserve is active.

  autoreload=True|False  reload the code if it changes. defaults to True


Examples:
  Run a "standard" CherryPy wsgi server--good for local development
    $ manage.py runwsgiserver

  Run a CherryPy server on port 80
    $ manage.py runwsgiserver port=80

  Run a CherryPy server as a daemon and write the spawned PID in a file, don't serve staticfiles or autoreload
    $ manage.py runwsgiserver daemonize=true pidfile=/var/run/django-cpwsgi.pid autoreload=False staticserve=False
  
  Run a CherryPy server using ssl with test certificates located in /tmp
    $ manage.py runwsgiserver ssl_certificate=/tmp/testserver.crt ssl_private_key=/tmp/testserver.key

  Run the wsgi server but serve all the static files from a single collected file tree
    $ manage.py collectstatic    # collects all the static files to STATIC_ROOT
    $ manage.py runwsgiserver staticserve=collectstatic

"""


CPWSGI_OPTIONS = {
'host': '127.0.0.1', # changed from localhost to avoid ip6 problem -clm
'port': 8000,   # changed from 8088 to 8000 to follow django devserver default
'server_name': 'localhost',
'threads': 10, 
'daemonize': False,
'workdir': None,
'pidfile': None,
'server_user': 'www-data',
'server_group': 'www-data',
'ssl_certificate': None,
'ssl_private_key': None,
# options useful for development - should these all be true by default or off by default?
'autoreload' : True,
'adminserve' : 'Deprecated',  
'staticserve' : True, # serve static
'servestaticdirs': True, # will use STATICFILES_DIRS and actuall serve each directory so
                          # you don't need to collect them all in development
'verbose' : 0,    
}

def change_uid_gid(uid, gid=None):
    """Try to change UID and GID to the provided values.
    UID and GID are given as names like 'nobody' not integer.

    Src: http://mail.mems-exchange.org/durusmail/quixote-users/4940/1/
    """
    if not os.geteuid() == 0:
        # Do not try to change the gid/uid if not root.
        return
    (uid, gid) = get_uid_gid(uid, gid)
    os.setgid(gid)
    os.setuid(uid)

def get_uid_gid(uid, gid=None):
    """Try to change UID and GID to the provided values.
    UID and GID are given as names like 'nobody' not integer.

    Src: http://mail.mems-exchange.org/durusmail/quixote-users/4940/1/
    """
    import pwd, grp
    uid, default_grp = pwd.getpwnam(uid)[2:4]
    if gid is None:
        gid = default_grp
    else:
        try:
            gid = grp.getgrnam(gid)[2]            
        except KeyError:
            gid = default_grp
    return (uid, gid)
    
def poll_process(pid):
    """
    Poll for process with given pid up to 10 times waiting .25 seconds in between each poll. 
    Returns False if the process no longer exists otherwise, True.
    """
    for n in range(10):
        time.sleep(0.25)
        try:
            # poll the process state
            os.kill(pid, 0)
        except OSError, e:
            if e[0] == errno.ESRCH:
                # process has died
                return False
            else:
                raise Exception
    return True

def stop_server(pidfile):
    """
    Stop process whose pid was written to supplied pidfile. 
    First try SIGTERM and if it fails, SIGKILL. If process is still running, an exception is raised.
    """
    if os.path.exists(pidfile):
        pid = int(open(pidfile).read())
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError: #process does not exist
            os.remove(pidfile)
            return
        if poll_process(pid):
            #process didn't exit cleanly, make one last effort to kill it
            os.kill(pid, signal.SIGKILL)
            #if still_alive(pid):
            if poll_process(pid):
                raise OSError, "Process %s did not stop."
        os.remove(pidfile)

def start_server(options):
    """
    Start CherryPy server

    Want SSL support?
    a. The new (3.1 or 3.2) way: Just set server.ssl_adapter to an SSLAdapter instance.
    b. The old way (deprecated way) is to set these attributes:

       server.ssl_certificate = <filename>
       server.ssl_private_key = <filename>

       But this is the only way from the management command line
       in the future I may need to adapt this to use a server.ssl_adapter

    """
    
    if options['daemonize'] and options['server_user'] and options['server_group']:
        #ensure the that the daemon runs as specified user
        change_uid_gid(options['server_user'], options['server_group'])
    
    from django_wsgiserver.wsgiserver import CherryPyWSGIServer 
    #from cherrypy.wsgiserver import CherryPyWSGIServer
    from django.core.handlers.wsgi import WSGIHandler
    app = WSGIHandler()
    # if options['adminserve']: # serve the admin media too
    #     # AdminMediaHandler is middleware for local use
    #     import django.core.servers.basehttp
    #     app = django.core.servers.basehttp.AdminMediaHandler(app)
        
    server = CherryPyWSGIServer(
        (options['host'], int(options['port'])),
        app,
        int(options['threads']), 
        options['server_name']
    )
    if options['ssl_certificate'] and options['ssl_private_key']:
        server.ssl_certificate = options['ssl_certificate']
        server.ssl_private_key = options['ssl_private_key']  
    try:
        logging.debug('starting server with options:\n%s' % pformat(options) )
        server.start()
    except KeyboardInterrupt:
        server.stop()

def process_staticfiles_dirs(staticfiles_dirs, default_prefix='/'): # settings.STATIC_URL
    """
    normalizes all elements of STATICFILES_DIRS to be of ('prefix','/root/path/to/files') form
    the prefix gets added after STATIC_URL
    """
    staticlocations=[]
    for staticdir in staticfiles_dirs:
        # elements of staticfiles_dirs are ether simple path strings like "/var/www/polls/static"
        # or are tuples/
        if isinstance(staticdir, (list, tuple)):
            prefix, root = staticdir
            root = os.path.abspath(root)
        else:
            # default url prefix used for single path elements
            root = os.path.abspath(staticdir)
            prefix = os.path.join(default_prefix, os.path.basename(root))+r'/' # end with /

        staticlocations.append((prefix, root))
    return staticlocations


class Command(BaseCommand):
    help = "CherryPy Server for project."
    args = "[various KEY=val options, use `runwsgiserver help` for help]"

    def handle(self, *args, **options):
        from django.conf import settings
        from django.utils import translation
        # Activate the current language, because it won't get activated later.
        try:
            translation.activate(settings.LANGUAGE_CODE)
        except AttributeError:
            pass
        self.runwsgiserver(args)
        
    def usage(self, subcommand):
        return CPWSGI_HELP

    def runwsgiserver(self, argset=[], **kwargs):
        # Get the options
        options = CPWSGI_OPTIONS.copy()
        options.update(kwargs)
        for x in argset:
            if "=" in x:
                k, v = x.split('=', 1)
            else:
                k, v = x, True
            if v=='False' or v=='false':
                v = False
                # print "found false", v
            options[k.lower()] = v

        self.options = options
        
        if "help" in options:
            print CPWSGI_HELP
            return

        if "stop" in options:
            stop_server(options['pidfile'])
            return True

        if options['daemonize']:
            options['autoreload'] = False # daemonize and autoreaload are not compatible currently
            if not options['pidfile']:
                options['pidfile'] = '/var/run/django_wsgi_%s.pid' % options['port']
            stop_server(options['pidfile'])     

            from django.utils.daemonize import become_daemon
            if options['workdir']:
                become_daemon(our_home_dir=options['workdir'])
            else:
                become_daemon()

            fp = open(options['pidfile'], 'w')
            fp.write("%d\n" % os.getpid())
            fp.close()

        # autoreload 
        if options['autoreload']:
            import django.utils.autoreload
            django.utils.autoreload.main(self.start_server_servestatic, (options,))
        else:
            # Start the webserver
            logging.info('starting server with options:\n%s' % pformat(options) )
            self.start_server_servestatic(options)


    def start_server_servestatic(self, options):
        """
        Start CherryPy server AND serve default static files

        Want SSL support?
        a. The new (3.1 or 3.2) way: Just set server.ssl_adapter to an SSLAdapter instance.
        b. The old way (deprecated way) is to set these attributes:

           server.ssl_certificate = <filename>
           server.ssl_private_key = <filename>

           But this is the only way from the management command line
           in the future I may need to adapt this to use a server.ssl_adapter

        """
        # debug?
        # print "options:"
        from django.conf import settings
        quit_command = (sys.platform == 'win32') and 'CTRL-BREAK' or 'CONTROL-C'

        self.stdout.write("Validating models..")
        self.validate(display_num_errors=True)
        self.stdout.write((
                "%(started_at)s\n"
                "Django version %(version)s, using settings %(settings)r\n"
                "cherrypy django_wsgiserver is running at http://%(addr)s:%(port)s/\n"
                "Quit the server with %(quit_command)s.\n"
            ) % {
                "started_at": datetime.now().strftime('%B %d, %Y - %X'),
                "version": self.get_version(),
                "settings": settings.SETTINGS_MODULE,
                "addr": options['host'], # self._raw_ipv6 and '[%s]' % self.addr or self.addr,
                "port": options['port'],
                "quit_command": quit_command,
            })

        #logger.info("launching wsgiserver with the following options")
        #logger.info(pformat(options))
        if int(options['verbose']) >= 2:
            self.stdout.write("launching with the following options:\n")
            self.stdout.write(pformat(options))

        if options['daemonize'] and options['server_user'] and options['server_group']:
            #ensure the that the daemon runs as specified user
            change_uid_gid(options['server_user'], options['server_group'])

        from django_wsgiserver.wsgiserver import CherryPyWSGIServer, WSGIPathInfoDispatcher
        #from cherrypy.wsgiserver import CherryPyWSGIServer, WSGIPathInfoDispatcher

        from django.core.handlers.wsgi import WSGIHandler
        from django.conf import settings
        app = WSGIHandler()  # serve the django content
        path = { '/': app}  # well will build up the serving url routing path below

        # Now work on serving the static content
        # note as of django 1.4, ADMIN_MEDIA_PREFIX is depreciated and instead uses django.contrib.staticfiles
        # so it is not an error for ADMIN_MEDIA_PREFIX to not be defined, I will test to see if exists
        # and print a warning that adminserve is activated but it's not defined.
        # so for django 1.4 (or 1.5 ?) staticserve=True => adminserve=True
        # so the choices
        # There are basically two ways for statics to be served
        # 1. in development, one often wants each application's static files to be served from within its file structure
        #    this is what the django runserver dose
        # 2. in production usually, all the static files are collected into a common storage region (files, S3, CDN) and a good webserver
        #    serve them from there

        # deprecated
        # if options['adminserve']: # serve the admin media too 
        #     # AdminMediaHandler is middleware for local use
        #     #import django.core.servers.basehttp
        #     #adminapp = django.core.servers.basehttp.AdminMediaHandler(app)
        #     # another way to serve the admin media three application
        #     if settings.__dict__.has_key('ADMIN_MEDIA_PREFIX'):
        #         import django.contrib.admin

        #         path[settings.ADMIN_MEDIA_PREFIX] = django_wsgiserver.mediahandler.StaticFileWSGIApplication(        
        #             os.path.join( django.contrib.admin.__path__[0], 'media'))
        #     else:
        #         print "Warning adminserve was selected BUT ADMIN_MEDIA_PREFIX was not defined"

        if options['staticserve']:
            try:
                if not settings.STATIC_URL or not settings.STATIC_ROOT:
                    # could use misconfigured exception (what is this in django)  instead of AttributeError
                    raise AttributeError, "settings.STATIC_URL = %s, settings.STATIC_ROOT=%s" % (repr(settings.STATIC_URL),
                                                                                                 repr(settings.STATIC_ROOT)) 
            except AttributeError, msg:
                logger.error(msg)
                logger.error("****")
                logger.error("STATIC_URL and STATIC_ROOT  must be set in settings file for staticserve option to work in django_wsgiserver")
                logger.error("****")
                raise

            if options['staticserve'] != 'collectstatic':
                if settings.STATICFILES_FINDERS: # find the apps' static files and add them to the path
                    logger.debug("see settings.STATICFILES_FINDERS")
                    logger.debug(pformat (settings.STATICFILES_FINDERS))
                    from django.contrib.staticfiles.finders import AppDirectoriesFinder
                    app_static_finder=AppDirectoriesFinder(settings.INSTALLED_APPS)
                    logger.debug("app_static_finder.storages:")
                    logger.debug(pformat(app_static_finder.storages))
                    for key,val in app_static_finder.storages.items():
                        logger.debug(key, " static location:", val.location)
                    # need to decide what to do with this in terms of the fusion of the app static directories
                        app_url=key.split('.')[-1] + r'/' # I'm not sure if it needs the end '/'
                        full_static_url = os.path.join(settings.STATIC_URL,app_url)
                        full_dir_location = os.path.join(val.location,app_url)
                        logger.debug(full_static_url, full_dir_location)
                        path[full_static_url] = django_wsgiserver.wsgiutil.StaticFileWSGIApplication(full_dir_location)


            if options['servestaticdirs'] and hasattr(settings, 'STATICFILES_DIRS'):
                staticlocations = process_staticfiles_dirs(settings.STATICFILES_DIRS)
                # debug !!!
                logger.debug("staticlocations::"); logger.debug(pformat(staticlocations))
                for urlprefix, root in staticlocations:
                    path[os.path.join(settings.STATIC_URL, urlprefix)] =  django_wsgiserver.wsgiutil.StaticFileWSGIApplication(root)

            # One important thing is that there are two different ways to serve the static files
            # 1. convenient: serve each app's static files (assuming they follow convention)
            # 2. do a collectstatic and serve from that node -- likely this would be done more in a "production" scenario

            if options['staticserve'] == 'collectstatic':
                # and serve the root of the STATIC_URL ? hmm !!!
                path[settings.STATIC_URL] = django_wsgiserver.wsgiutil.StaticFileWSGIApplication(settings.STATIC_ROOT)
                logger.warning("serving all static files from %s. *** Make sure you have done a fresh collectstatic operation ***" % settings.STATIC_ROOT)

        # debug
        logger.debug("path:", pformat(path))
        dispatcher =  WSGIPathInfoDispatcher( path )
        logger.debug("apps:", pformat(dispatcher.apps))

        if options['verbose'] == '1':
            from django_wsgiserver.wsgiutil import WSGIRequestLoggerMiddleware
            dispatcher = WSGIRequestLoggerMiddleware(dispatcher)
            logger.setLevel(10)
            
        if int(options['verbose']) >= 2:
            from django_wsgiserver.wsgiutil import WSGIRequestLoggerMiddleware
            dispatcher = WSGIRequestLoggerMiddleware(dispatcher)
            logger.setLevel(logging.INFO)

            
        server = CherryPyWSGIServer(
            (options['host'], int(options['port'])),
            dispatcher,
            int(options['threads']), 
            options['server_name']
        )
        if options['ssl_certificate'] and options['ssl_private_key']:
            Adapter = wsgiserver.get_ssl_adapter_class()
            try:
                server.ssl_adapter = Adapter(certificate=options['ssl_certificate'],
                                            private_key=options['ssl_private_key'])
            except ImportError:
                pass # because we can try again
            try:
                Adapter = wsgiserver.get_ssl_adapter_class('builtin')
                server.ssl_adapter = Adapter(certificate=options['ssl_certificate'],
                                             private_key=options['ssl_private_key'])
            except ImportError:
                Adapter = None
                raise
        try:
            server.start()
        except KeyboardInterrupt:
            server.stop()

        



