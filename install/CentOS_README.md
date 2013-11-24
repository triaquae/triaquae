

安装依赖环境
yum install gcc gcc-c++ make sysstat nc -y
yum install python-devel -y
yum install net-snmp net-snmp-utils net-snmp-devel -y
yum install mysql mysql-server mysql-devel -y
/etc/init.d/mysqld start


安装rrdtool
yum install cairo-devel libxml2-devel pango-devel pango libpng-devel freetype freetype-devel libart_lgpl libart_lgpl-devel intltool -y
yum install rrdtool rrdtool-devel -y


升级python为2.7以上
python -V
sh install/python_ins27.sh
python -V
说明：5.x系统python默认版本是2.4。安装包中自带升级python 2.7的脚本,安装完成后在次检查python版本


安装TriAquae
tar zxf TriAquae.tar.gz
cd TriAquae/install
python setup.py build --prefix=/opt/soft/TriAquae
python setup.py install

修改数据库和IP
修改tri_config配置文件
MySQL_Name = 'TriAquae'
MySQL_User = 'root'
MySQL_Pass = 'coral'
Tri_IP = '192.168.2.2'
配置报警接受邮件
SMTP_server = 'smtp.company.com' #replace it to your company smtp server
Mail_username = 'mailuser'
Mail_password = 'mailpass'


初始化
python setup.py init


启动TriAquae
cd /your installdir/TriAquae/sbin
python tri_service.py start
说明：启动默认为7000端口


登陆TriAquae
http://ip:7000/
默认账户：admin
默认密码：triaquae
注意：关闭iptables


FAQ
1、启动tri_service.py时报导入错误
ImportError: libpython2.7.so.1.0: cannot open shared object file: No such file or directory
解决方法：
  升级为python2.7

2、登陆堡垒机连接远程服务器不显示连接信息，无任何输出
解决方法：
  logs目录需要777权限

3、执行$ sudo python tri_service.py start
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: libmysqlclient_r.so.15: cannot open shared object file: No such file or directory
解决方法：
  访问https://pypi.python.org/simple/MySQL-python/下载合适的MySQLdb版本进行编译安装




