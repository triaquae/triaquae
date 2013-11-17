#!/usr/bin/env python
# -*- coding: utf-8 -*-
# fix these up
import os, stat, mimetypes
import django
from django.utils.http import http_date
from django.conf import settings

import logging
logger = logging.getLogger('django_wsgiserver')

class BlockIteratorResponse(object):
    status_code = 200
    # Vlada Macek Says:
    # September 29th, 2009 at 14:42
    # You’re handing the static files by

    #                output = [fp.read()]
    #                fp.close()

    # which causes entire content is loaded to the memory (and not only once
    # by my observation). This is unacceptable for large files. I found this
    # to be much more memory & CPU efficient:

    def __init__(self, fp):
        self.fp = fp
        
    def __iter__(self):
           return self

    def next(self):
        chunk = self.fp.read(20*1024)
        if chunk:
            return chunk
        self.fp.close()
        raise StopIteration

class SimpleResponse(list):
    # you know I could just use the code in django.http.response e.g. HttpResponse object -clm
    # this has already defined responses for codes 301,302,304, 400, 403, 404, 405, 410, 500
    """allow for simple responses in WSGI stacks
        use like a list but set the status_code of the response"""
    status_code = 0

    
class StaticFileWSGIApplication( object ):

    def __init__( self, static_file_root ):
        self.static_file_root = os.path.normpath(static_file_root)

    def __call__( self, environ, start_response ):

        def done( status, headers, output ):
            # a good place for debug loging 
            # e.g. logger.debug('done from self.static_file_root: %s' %self.static_file_root, status, headers)
            start_response( status, headers.items() )
            return output

        path_info = environ['PATH_INFO']
        if path_info[0] == '/':
            path_info = path_info[1:]
        file_path = os.path.normpath( os.path.join( self.static_file_root, path_info ) )

        # prevent escaping out of paths below media root (e.g. via "..")
        if not file_path.startswith( self.static_file_root ):
            status = '401 UNAUTHORIZED'
            headers = {'Content-type': 'text/plain'}
            output = ['Permission denied. illegal path'] 
            return done( status, headers, output )

        # only allow GET or HEAD requests e.g. not PUT, DELETE, POST, etc.
        if not (environ['REQUEST_METHOD'] == 'GET' or environ['REQUEST_METHOD'] == 'HEAD'):
            status = '405 METHOD NOT ALLOWED'
            headers = {'Content-type': 'text/plain'}
            output = SimpleResponse(['405 method not allowed'])
            output.status_code = 405
            return done(status, headers, output)
        
        if not os.path.exists( file_path ):
            status = '404 NOT FOUND'
            headers = {'Content-type': 'text/plain'}
            output = SimpleResponse(['Page not found: %s' % file_path])
            output.status_code = 404
            return done( status, headers, output )

        try:
            fp = open( file_path, 'rb' )
        except IOError:
            status = '401 UNAUTHORIZED'
            headers = {'Content-type': 'text/plain'}
            output = SimpleResponse(['Permission denied: %s' % file_path])
            output.status_code = 401
            return done( status, headers, output )

        # This is a very simple implementation of conditional GET with
        # the Last-Modified header. It makes media files a bit speedier
        # because the files are only read off disk for the first request
        # (assuming the browser/client supports conditional GET).

        # mtime needs to be ascii not unicode as django is all unicode need to do conversion
        mtime = http_date( os.stat(file_path)[stat.ST_MTIME] ).encode('ascii', 'ignore') 
        headers = {'Last-Modified': mtime}
        if environ.get('HTTP_IF_MODIFIED_SINCE', None) == mtime:
            status = '304 NOT MODIFIED'
            output = SimpleResponse() 
            output.status_code = 304
        else:
            status = '200 OK'
            mime_type = mimetypes.guess_type(file_path)[0]
            if mime_type:
                headers['Content-Type'] = mime_type

            # naive version with whole file read as a string place in a list
            # output = [fp.read()]
            # fp.close()
            # use BlockIteratorResponse for larger file/network efficiency
            output = BlockIteratorResponse(fp)
            
        return done( status, headers, output )


class WSGIRequestLoggerMiddleware(object):
    # based upon class WSGIPathInfoDispatcher(object):
    """

    A WSGI middle ware to printout/log the requests and response codes

    """

    def __init__(self, app):
        self.wsgiapp = app

    def __call__(self, environ, start_response):
        output = self.wsgiapp(environ, start_response)
        #pprint(environ)
        if hasattr(output, 'status_code'):
            logger.log(10, "[%s] %s %s" % (environ['REQUEST_METHOD'], environ['REQUEST_URI'], output.status_code))
        else:
            logger.log(10, "[%s] %s %s" % (environ['REQUEST_METHOD'], environ['REQUEST_URI'], repr(output) ))
        return output


