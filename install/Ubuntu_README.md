
安装依赖环境
sudo apt-get install gcc make sysstat nc
sudo apt-get install python-dev
sudo apt-get install snmpd
sudo apt-get install mysql-client mysql-server
sudo apt-get install python-mysqldb
sudo /etc/init.d/mysql start


安装rrdtool
sudo apt-get install rrdtool


安装TriAquae
sudo tar zxf TriAquae.tar.gz
cd TriAquae/install
sudo python setup.py build --prefix=/opt/soft/TriAquae
sudo python setup.py install

修改数据库和IP
修改tri_config配置文件
MySQL_Name = 'TriAquae'
MySQL_User = 'root'
MySQL_Pass = 'coral'
Tri_IP = '192.168.2.2'
配置报警接受邮件
SMTP_server = 'smtp.126.com'
Mail_username = 'mailuser'
Mail_password = 'mailpass'

初始化
sudo python setup.py init

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

