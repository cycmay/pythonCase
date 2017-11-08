# -×- coding: utf-8 -*-

import os
import time

source = ['/home/cyc/文档/pyt/']
target_dir = '/home/cyc/桌面/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_commmand = "zip -qr %s %s" %(target,''.join(source))

if os.system(zip_commmand) == 0:
	print('Successful backup')
else:
	print('Backup Failed')

#-q zip命令安静工作
#-r 表示zip命令进行目录递归工作
#time模板
#string.join(表),将string加到表中，所有空隙都加
#本程序将所有命令添加到zip_command一行中，调用os.system()函数运行，如果成功，返回0
