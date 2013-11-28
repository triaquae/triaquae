TriAquaue文档
==============

安装依赖环境
--------------

	yum install gcc gcc-c++ make sysstat nc -y
	
	yum install python-devel -y
	
	yum install net-snmp net-snmp-utils net-snmp-devel -y
	
	yum install mysql mysql-server mysql-devel -y
	
	/etc/init.d/mysqld start



安装rrdtool
-----------
	yum install cairo-devel libxml2-devel pango-devel pango libpng-devel freetype freetype-devel libart_lgpl libart_lgpl-devel intltool -y

	yum install rrdtool rrdtool-devel -y



升级python为2.7以上
-----------------

	python -V

	sh install/python_ins.sh

	python -V

说明：5.x系统python默认版本是2.4。安装包中自带升级python 2.7的脚本,安装完成后在次检查python版本



	tar zxf TriAquae.tar.gz

	cd TriAquae/install

	python setup.py build --prefix=/opt/soft/TriAquae

	python setup.py install


修改数据库和IP
----------------

修改tri_config配置文件

	MySQL_Name = 'TriAquae'

	MySQL_User = 'root'

	MySQL_Pass = 'coral'

	Tri_IP = '192.168.2.2'



配置报警接受邮件
--------------

	SMTP_server = 'smtp.company.com' #replace it to your company smtp server

	Mail_username = 'tri_mailuser'

	Mail_password = 'Motherfucker!23'


初始化
------

	python setup.py init



启动TriAquae
------------

	cd /your installdir/TriAquae/sbin

	python tri_service.py start

说明：启动默认为7000端口



登陆TriAquae

http://ip:7000/

默认账户：admin

默认密码：triaquae

注意：关闭iptables

开发者模式
---------
仅限开发者方便使用：

	python setup_dev.py init    #初始化数据库



FAQ
-----
> 1、跳板机不显示连接信息::
>>logs目录需要777权限