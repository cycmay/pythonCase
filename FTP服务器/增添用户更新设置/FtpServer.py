# --*-- coding:utf-8 --*--

#实现简单的本地验证
import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from conf import setting




#添加匿名用户，只需要路径
#authorizer.add_anonymous('/home/ubuntu')




def get_user(userfile):

	user_list = []
	with open(userfile) as file:
		#print(len(line.split()))
		for line in file:
			if not line.startswith('#') and line:
				if len(line.split()) == 4:
					user_list.append(line.split())
				else:
					print('user.conf配置错误！')

	return user_list

def main():
	#实例化虚拟用户，这是FTP验证的首要条件
	authorizer = DummyAuthorizer()

	#添加用户
	user_list = get_user('conf/user.py')

	for user in user_list:
		name,password,permit,homedir = user
		try:
			#添加用户权限和路径，括号内的参数是（用户名，密码，用户目录，权限）
			authorizer.add_user(name,password,homedir,perm = 'elradfmw')
		except Exception as e:
			print(e,'44')

	#初始化ftp句柄
	handler = FTPHandler
	handler.authorizer = authorizer

	#日志记录
	if setting.enable_logging == 'on':
		logging.basicConfig(filename = setting.logging_name,level = logging.INFO)

	#欢迎信息
	handler.banner = setting.welcome_msg

	#添加被动端口范围
	handler.passive_ports = range(setting.passive_ports[0], setting.passive_ports[1])

	#监听ip 和端口，因为linux里非root用户无法使用21端口，所以使用2121端口
	server = FTPServer((setting.ip, setting.port),handler)

	#最大连接数
	server.max_cons = setting.max_cons
	server.max_cons_per_ip = setting.max_per_ip

	#开始服务
	print('START！。。。')
	server.serve_forever()

if __name__ == '__main__':
		main()