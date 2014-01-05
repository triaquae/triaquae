from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
#from models import Devinfo, Check_Devinfo, ServerStatus, DevForm
#from models import Group,IP,RemoteUser,OpsLog,OpsLogTemp,TriaquaeUser,AuthByIpAndRemoteUser,QuickLink
#from models import *

from TriAquae.backend import MultiRunCounter
#from backend import MultiRunCounter

import datetime, os, time
import json
from TriAquae.backend import tri_config
from django.core import serializers

#start by zp
yesterday = (datetime.datetime.now()-datetime.timedelta(days=2)).strftime("%Y-%m-%d")

def index(request):
    up = ServerStatus.objects.filter(host_status='UP').count()
    down = ServerStatus.objects.filter(host_status='DOWN').count()
    total = ServerStatus.objects.all().count()
    if total == 0:
        percent = 0
    else:
        percent = round(up / float(total), 4) * 100
    context = {'up':up, 'down':down, 'total':total, 'percent':percent }
    return render(request,'index.html', context)
@login_required
def assets(request):
    latest_host_list = Devinfo.objects.order_by('-id')
    auto_check  = Check_Devinfo.objects.filter(Change_Time__gte=yesterday, Change_Time__lte=datetime.date.today()).count()
    #auto_check  = '2'
    context = { 'latest_host_list':latest_host_list, 'auto_check':auto_check }
    return render(request, 'assets_management.html', context)

@login_required
def assets_detail(request, id):
    host = Devinfo.objects.get(pk=id)
    form = DevForm(instance=host)
    return render(request, 'assets_detail.html', {'host':host, 'form':form}, context_instance=RequestContext(request))

@login_required
def assets_diff(request):
    latest_host_list = Check_Devinfo.objects.filter(Change_Time__gte=yesterday, Change_Time__lte=datetime.date.today())
    context = { 'latest_host_list':latest_host_list }
    return render(request, 'assets_diff.html', context)

@login_required
def status(request):
    from pprint import pprint
    group_dic = {}
    json_dict = {}
    for group_name in Group.objects.all():
        ip_list = IP.objects.filter(group__name=group_name.name)
        server_status_list={}
        server_status_json = {}
        for host in ip_list:
	   try:
            	ip_status = ServerStatus.objects.get(hostname=host.hostname)
           except ObjectDoesNotExist:
		print "Ip not ServerStatus table",host 
		continue
	   server_status_list[host]=ip_status
           last_check = ip_status.last_check
           server_status_json[host.ip]=json.loads(serializers.serialize('json', [ip_status]))[0]
           #server_status_json[host.ip]['fields']['last_check'] = last_check.strftime('%Y-%m-%d %H:%M:%S')
	group_show_name = '%s [%s]' %(group_name.name,len(server_status_list))
        group_dic[group_show_name] = server_status_list
        json_dict[group_show_name ] = server_status_json
    context = { 'group_dic':group_dic }
    if request.is_ajax():
	#print json_dict
        return HttpResponse(json.dumps(json_dict), mimetype="application/json")
    return render(request, 'server_status.html', context)

@login_required
def status_detail(request,hostname):
    host = ServerStatus.objects.get(hostname=hostname)
    #TriaquaeUser_remote_users = str(TriaquaeUser.objects.get(user__username=request.user).remoteuser.all())
    TriaquaeUser_remote_users = []
    for user in TriaquaeUser.objects.get(user__username=request.user).remoteuser.all():
        TriaquaeUser_remote_users.append(str(user))
    #AuthByIpAndRemoteUser_remote_user = set([m.remoteUser.name for m in AuthByIpAndRemoteUser.objects.all()])
    AuthByIpAndRemoteUser_remote_user = []
    #for user in AuthByIpAndRemoteUser.objects.all():
    for user in AuthByIpAndRemoteUser.objects.filter(ip__ip=host):
        AuthByIpAndRemoteUser_remote_user.append(str(user.remoteUser))
    remote_users = set(TriaquaeUser_remote_users) & set(AuthByIpAndRemoteUser_remote_user)
    tri_user,tri_pass = tri_config.Tri_connector_username,tri_config.Tri_connector_password 
    try:
    	assets = Devinfo.objects.get(Triaquae_Hostname=hostname)
    except ObjectDoesNotExist:
	assets = None
    
    ip = host.host
    rrd_dir = tri_config.RRDTOOL_png_dir
    rrd_list = os.listdir(rrd_dir)
    rrd_file_list_1hour = [i for i in rrd_list if (i.startswith(ip) and i.endswith('1h.png'))]
    rrd_file_list_1day = [i for i in rrd_list if (i.startswith(ip) and i.endswith('1d.png'))]
    return render(request, 'status_detail.html', {'host':host, 'assets':assets, 'tri_user':tri_user,'tri_pass':tri_pass, 'remote_user':remote_users,'rrd_dir':rrd_dir,'rrd_file_list_1hour':rrd_file_list_1hour,'rrd_file_list_1day':rrd_file_list_1day}, context_instance=RequestContext(request))
    '''
    if request.is_ajax():
        from django.core import serializers
        serialized_host = serializers.serialize('json', [ host, assets,])
        #serialized_host = serializers.serialize('json', [ host,])
        #serialized_assets = serializers.serialize('json', [ assets,])
        return HttpResponse(serialized_host, mimetype="application/json")
        #return HttpResponse(serialized_assets, mimetype="application/json")
    '''
    #return render(request, 'status_detail.html', {'host':host, 'rrd_dir':rrd_dir,'rrd_file_list':rrd_file_list}, context_instance=RequestContext(request))


#end by zp

#start by tangjing
@login_required
def command_execution(request):
    t = get_template('command_execution.html')
    #html=t.render(Context({'form_name':'Enter your command:'}))
    html=t.render(Context({'user':request.user}))
    return HttpResponse(html)

@login_required
def file_transfer(request):
    t = get_template('file_transfer.html')
    html=t.render(Context({'user':request.user}))
    return HttpResponse(html)
@login_required
def GetServers(request):
    data = []
    counter = 0
    group_list  = Group.objects.all()
    group_list2 = TriaquaeUser.objects.get(user__username=request.user.username).group.values('name')

    for g in group_list2:
	g_name = g['name']
        counter += 1
	ip_nums_in_group = IP.objects.filter(group__name = g_name).count()
        data.append({'id': counter, 'pid':0, 'text':'%s [%s]' %(g_name,ip_nums_in_group), 'bgroup':1})
        ip_list =  IP.objects.filter(group__name = g_name)
        ip_counter = 0
        for ip in ip_list:
            ip_counter += 1
            data.append({'id':'%s%s'%(counter,ip_counter), 'pid': counter, 'text':ip.hostname,       'bgroup':0 , 'ip':ip.ip })

        '''data=[
         { 'id':1,'pid':0, 'text': 'Node 1','bgroup':1},
         { 'id':11,'pid':1, 'text': 'Node 1.1','bgroup':0},
         { 'id':12,'pid':1, 'text': 'Node 1.2','bgroup':0},
         { 'id':2,'pid':0,'text': 'Node 2' ,'bgroup':0},
         { 'id':3,'pid':0,'text': 'Node 3' ,'bgroup':0},
         { 'id':4,'pid':0,'text': 'Node 4' ,'bgroup':0},
         { 'id':5,'pid':0,'text': 'Node 5' ,'bgroup':0},
         ];'''
    else:
	ip_list = TriaquaeUser.objects.get(user__username=request.user.username).ip.values('ip','hostname')
        other_ip_nums =len(ip_list)
	counter +=1
	data.append({'id': counter, 'pid':0, 'text':'Others [%s]' %other_ip_nums, 'bgroup':1})
	ip_counter = 0
	for ip in  ip_list:
		ip_counter += 1
		data.append({'id':'%s%s'%(counter,ip_counter), 'pid': counter, 'text':ip['hostname'],       'bgroup':0 , 'ip':ip['ip'] })
    return HttpResponse(json.dumps(data))



def LogIn(request):
    if request.user is not None:
        logout_view(request)
    t = get_template("login.html")
    html = t.render(Context())
    return HttpResponse(html)
#
def account_auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    tri_user = auth.authenticate(username=username,password=password)
    if tri_user is not None:
	auth.login(request,tri_user)
	return HttpResponseRedirect('/showDashboard')
    else:
	return render_to_response('login.html',{'login_err':'Wrong username or password!'})
#
@login_required
def showDashboard(request):
    return render_to_response('index.html',{'user':request.user , 'quick_links': QuickLink.objects.all()})
def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("%s logged out!" % user)
def hello(request):
  if request.user.is_authenticated() is None:
	return HttpResponse("User not login yet!!!")
  else:

	now = datetime.datetime.now()
	group_list ={}
	for group in Group.objects.all():
		ip_nums_in_group = IP.objects.filter(group__group_name = group)
		group_list[group] = ip_nums_in_group

	return render_to_response("boot1.html",{'group_list':group_list, 'user':request.user})
	#return render_to_response('hello.html',{'current_date': now} )

@login_required
def batch_management(request):
  if request.user.is_authenticated() is None:
        return HttpResponse("User not login yet!!!")
  else:

        now = datetime.datetime.now()
        group_list ={}
        for group in Group.objects.all():
                ip_nums_in_group = IP.objects.filter(group__group_name = group)
                group_list[group] = ip_nums_in_group
	RemoteUsers = RemoteUser.objects.all()
	return render_to_response("BatchManagement.html",{'group_list':group_list, 'user':request.user,'r_users':RemoteUsers})
#return HttpResponse('{"success_tasks":%s,"failed_tasks":%s,"cmd_log":[%s]}' %(success_tasks,failed_tasks,cmd_ret))
@login_required
def cmd_result(request):
                track_id = request.GET['TrackMark']
                total_tasks = request.GET['TotalTasks']
                success_tasks= OpsLog.objects.get(track_mark = track_id).success_num
                failed_tasks = OpsLog.objects.get(track_mark = track_id).failed_num

		command_result = OpsLogTemp.objects.filter(track_mark = track_id)
		data_dic = {}
		for ip in command_result:
			data_dic[ip.ip] = [ip.ip, ip.user,  ip.event_log,  ip.result ]

		data_dic['result_count'] = [success_tasks, failed_tasks]
        	return HttpResponse(json.dumps(data_dic))
@login_required
def get_groupList(request):
	if request.is_ajax():
	        #if request_method == "GET":
		G_name = request.GET['Name']
		ip_list = IP.objects.filter(group__group_name = G_name)

	return render_to_response('server_list.html',{"ip_list_of_group":ip_list},context_instance=RequestContext(request))

@login_required
def runCmd(request):
    track_mark = MultiRunCounter.AddNumber()
    user_input = request.POST['command']
    user_account = request.POST['UserName']
    iplists = request.POST['IPLists'].split(',')

    task_num = len(set(iplists))
    print "user input command is: %s and username is:%s and iplists are: %s" %(user_input,user_account,' '.join(iplists))
    cmd = "python %s/TriAquae/backend/multiprocessing_runCMD2.py %s '%s' '%s' %s &" % (tri_config.Working_dir,track_mark,' '.join(iplists),user_input,user_account)
    os.system(cmd)
    return HttpResponse('{"TrackMark":%s, "TotalNum":%s}' %(track_mark, task_num))

@login_required
def getFailedLists(request):
	track_id = request.GET['TrackMark']
	fail_list = OpsLogTemp.objects.filter(track_mark = track_id,result ="Error")
	ip_list = []
	for ip in fail_list:
		ip_list.append(ip.ip)
        return HttpResponse(json.dumps(ip_list))
@login_required
def getSuccessLists(request):
	track_id = request.GET['TrackMark']
	ret_list = OpsLogTemp.objects.filter(track_mark = track_id,result = "Success")
	ip_list = []
	for ip in ret_list:
		ip_list.append(ip.ip)
	return HttpResponse(json.dumps(ip_list))

@login_required
def AllUsers(request):
	print request.user
	#loginuser = request.GET['LoginUser']
	#user_list = RemoteUser.objects.all() #TriaquaeUser.objects.get(user__username=request.user)
	user_list = TriaquaeUser.objects.get(user__username=request.user.username).remoteuser.values('name')
	print user_list
	u_list = []
	if user_list is not None:
		for u in user_list:
			u_list.append(u['name'])
	return HttpResponse(json.dumps(u_list))

@login_required
def AllCommands(request):
        cmd_list = os.popen('bash %s/TriAquae/backend/command_list.sh' %tri_config.Working_dir ).read()
        #commands = cmd_list.split('\n')
        return HttpResponse(cmd_list)

@login_required
def stopExecution(request):
	trackmark = request.GET['TrackMark']
	#todo
	cmd = '''ps -ef |grep -v grep |grep "multiprocessing_runCMD2.py %s" |awk '{print $2}'|xargs kill -9''' % trackmark
	print cmd
	os.system(cmd)
	return HttpResponse("stop successfully")

@login_required
def getFileLists(request):
	SftpSendDir = tri_config.Tri_sftp_send_dir 

	file_list = os.listdir(SftpSendDir)
	list_dic = {}
	for f in file_list:
		if os.path.isdir('%s/%s' %(SftpSendDir,f))  is True:
			d = os.popen('du -sh %s/%s ' %(SftpSendDir,f))
			f_size = d.read().split('\t')[0]
			f_type = 'dir'
			list_dic[f] = [f_size,f_type]
		else:
			f_size ='%sBit'% os.lstat('%s/%s' %(SftpSendDir,f)).st_size
			f_type = 'file'
			list_dic[f] = [f_size,f_type]

	return HttpResponse(json.dumps(list_dic))

@login_required
def transfer_file(request):
	ip_list = request.POST['IPLists'].split(',')
	print ip_list
	ip_list_to_string = ' '.join(ip_list)
	print ip_list_to_string
	option = request.POST['command']
	remote_user = request.POST['UserName']
	track_mark = MultiRunCounter.AddNumber()
	if option == 'SendFile':
		local_path = tri_config.Tri_sftp_send_dir 
	        file_list = request.POST['FileLists'].split(',')
		print file_list
		remote_path = request.POST['RemotePath']
		def compress(source_file_list):
			format_file_list = []
			for f in source_file_list:
				format_file_list.append(f)
			file_list_to_string = ' '.join(format_file_list)
			os.chdir(local_path)
			compressed_file = time.strftime('/tmp/TriSFTP_send_file_%Y%m%d_%H_%M_%S.tgz')
			cmd = "tar cvzf %s %s" %(compressed_file,file_list_to_string)
			os.system(cmd)
			file_size = os.stat(compressed_file).st_size
			return compressed_file
		transfer_action = "python  %s/TriAquae/backend/multiprocessing_sftp2.py %s %s -s %s %s '%s' &" %(tri_config.Working_dir,track_mark,remote_user,compress(file_list),remote_path,ip_list_to_string)
	elif option == 'GetFile':
		local_path = tri_config.Tri_sftp_recv_dir 
		remote_file = request.POST['RemotePath']
		transfer_action = "python  %s/TriAquae/backend/multiprocessing_sftp2.py %s %s -g %s '%s' &" %(tri_config.Working_dir,track_mark,remote_user,remote_file,ip_list_to_string)

	os.system(transfer_action)
	total_task = len(set(ip_list))
        return HttpResponse('{"TrackMark":%s, "TotalNum":%s}' %(track_mark,total_task))

@login_required
def getDangerousCmd(request):
	dangerous_filename = '%s/TriAquae/backend/dangerous_cmd.txt' % tri_config.Working_dir
	f= file(dangerous_filename)
	cmd_list = f.read().split('\r\n')
	print cmd_list
	return HttpResponse(json.dumps(cmd_list))
@login_required
def getCPUInfo(request):
	b = os.popen("sar 1 1 | grep Average| awk '{print $3,$5}'").read()
       	b = b.split()
	user = float(b[0])
        system = float(b[1])
	print "user and system are ",user,system
	return HttpResponse('{"user": %s,"system":%s}' % (user,system))
def getAverageLoad(request):
        load = os.popen("uptime").read()
        load_list = load.strip('\n').split("load average:")[1].strip().split(',')
        min_1 = load_list[0]
	min_5 = load_list[1]
        return HttpResponse('{"min_1": %s, "min_5":%s}' % (min_1,min_5))
@login_required

def getMemInfo(request):
	m = os.popen("free -m |grep '^Mem'|awk '{print $2, $3 - $6 - $7 }' ").read()
	b = m.split()
	total_mem = b[0]
	used_mem = b[1]
	print 'total_mem',total_mem, 'used', used_mem
	return HttpResponse('{"total_mem":%s,"used_mem": %s}' %(total_mem,used_mem))


@login_required
def getServerUpDownNum(request):
	up = ServerStatus.objects.filter(host_status='UP').count()
	down = ServerStatus.objects.filter(host_status='DOWN').count()
	total = ServerStatus.objects.all().count()
	return HttpResponse('{"total_server":%s,"up_server":%s,"down_server":%s}' %(total,up,down))









def baoleihost_remote(request):
    #python /server/scripts/py/django/Coral/web01/scripts/baoleihost.py 10.0.0.66 22 coral SSH_PASSWD 1

    triaquae_path = tri_config.Working_dir
    profile_file = "%s/TriAquae/logs/%s_profile" % (triaquae_path,request.user)
    #baoleihost_file = "%s/TriAquae/backend/baoleihost.py" % triaquae_path
    baoleihost_file = tri_config.Tri_connector_baoleihost

    remote_ip = request.GET['ip']
    remote_user = request.GET['user']
    print remote_ip
    print remote_user
    remote_login_server = AuthByIpAndRemoteUser.objects.get(ip__ip=remote_ip,remoteUser__name=remote_user)
    print remote_login_server.authtype, remote_login_server.password,'===============alex'
    protocol_type = remote_login_server.authtype
    password = remote_login_server.password
    key_path = remote_login_server.password
    port = IP.objects.get(ip=remote_ip).port
    if protocol_type == "ssh":
            protocol = "SSH_PASSWD"
            cmd = "python %s %s %s %s %s %s %s\n" % (baoleihost_file,remote_ip,port,remote_user,protocol,password,request.user)
    elif protocol_type == "ssh-key":
            protocol = "SSH_KEY"
            cmd = "python %s %s %s %s %s %s %s\n" % (baoleihost_file,remote_ip,port,remote_user,protocol,key_path,request.user)
    print cmd

    '''record TriAquae user profile'''
    #print profile_file
    f = open(profile_file,'w')
    f.write(cmd)
    f.flush()
    f.close()

    '''start local shellinabxd'''
    #ipaddr = "118.244.168.45"
    ipaddr = tri_config.Tri_IP
    shellinaboxd_port = int(4200)
    url = 'http://%s:%s/' % (ipaddr,shellinaboxd_port)
    #url = 'https://%s:%s/' % (ipaddr,shellinaboxd_port)
    #return HttpResponseRedirect(url)
    #return render_to_response("BatchManagement.html",{'group_list':group_list, 'user':request.user,'r_users':RemoteUsers})
    username = tri_config.Tri_connector_username
    password = tri_config.Tri_connector_password
    boxInfo = {'url':url,'username':username,'password':password}
    return HttpResponse(json.dumps(boxInfo))



def Log(request):
    return render_to_response("log_date.html")

def LogView(request):
    date = request.GET['date']
    log_date = date.replace('-','_')
    log_file = "%s/TriAquae/logs/audit_%s_%s.log" % (tri_config.Working_dir,log_date,request.user)
    print log_file
    try:
        # f = open(log_file,'r')
        f = open('audit_2013_09_05_alex.log')

        list = []
        dict = {}
        for line in f.readlines():
            line = line.split('|')
            new_line = {'Remote_Ip':line[0],'Date':line[1],'User':line[2],'Command':line[3]}
            list.append(new_line)
        
        res={'cols':['Remote_Ip','Date','User','Command'],'arr':list}

        f.close()
        t = Template(
        '''
        \n<h3 style="color:red">\t\tDATE: {{date}}\t\tUser: {{user}}</h3>
        \n<pre>{{content}}</pre>
        '''
        )
        html = t.render(Context({'date':date,'user':request.user,'content':json.dumps(res)}))
        print content
        print html
        #return HttpResponse(html)
        return render_to_response("log_date.html",{"content":html})
    except IOError:
        content = "%s No Record" % log_file
        return render_to_response("log_date.html",{"content":content})







