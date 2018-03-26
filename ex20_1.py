# --coding: utf-8 --
#导入模块sys的argv变量
#读取我输入的名字当指定文件中
from sys import argv
script,filename = argv
myname =  raw_input("your_name:")
myname += raw_input("your_age:")
perinfo = open(filename,'w')
perinfo.write(myname)
#print perinfo.read()
#perinfo.close()


