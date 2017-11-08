# -*- coding:utf-8 -*-

import os
import time

source = ['/home/cyc/文档/pyt/']
target_dir = '/home/cyc/桌面/'

today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime('%H%M%S')

touch = today_dir + os.sep +time_dir +'.zip'

commmand_touch = "zip -qr " + touch + ' ' + ' '.join(source)

if os.path.exists(today_dir) == 0:
	os.mkdir(today_dir)
if os.system(commmand_touch) == 0:
	print('Successful backup')
else:
	print('Backup Failed')
