#-*- coding:utf-8 -*-

#tkinter界面编程
'''
	tkinter介绍，python模块，调用tcl/tk接口,跨平台的脚本图形界面接口，性能不太好

	
'''
import tkinter
import os
import time

def backup():
	global entry_source
	global entry_target
	source = entry_source.get()
	target_dir = entry_target.get()

	today_dir = target_dir + time.strftime('%Y%m%d')
	time_dir = time.strftime('%H%M%S')

	touch = today_dir + os.sep + time_dir + '.zip'
	command_touch = "zip -qr " + touch + ' ' + source

	print(command_touch)
	print(source)
	print(target_dir)

	if os.path.exists(today_dir) == 0:
		os.mkdir(today_dir)
	if os.system(command_touch)==0:
		print('Success !')
	else:
		print('Failed!')

#设计界面
root = tkinter.Tk()
root.title('BackUp')
root.geometry('500x200')

lbl_source = tkinter.Label(root,text='source')
lbl_source.grid(row=0,column=0)
entry_source = tkinter.Entry(root)
entry_source.grid(row=0,column=1)

lbl_target = tkinter.Label(root,text='Target')
lbl_target.grid(row=1,column=0)
entry_target = tkinter.Entry(root)
entry_target.grid(row=1,column=1)

but_back = tkinter.Button(root,text='BackUp')
but_back.grid(row =3,column=0)
but_back["command"]=backup
root.mainloop()