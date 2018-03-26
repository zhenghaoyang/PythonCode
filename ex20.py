# --coding: utf-8 --
#导入模块sys的argv变量
from sys import argv
#解包
script,input_file = argv
#定义一个接受文件的函数
def print_all(f):
#打印出接受文件的本文
    print f.read()
#定义一个接受文件的函数
def rewind(f):
#将文件指针跳转到其实位置
    f.seek(0,0)
#接受两个参数，打印出来
def print_a_line(line_count,f):
    print line_count,f.readline()
#使用open函数打开文件，返回这个文件
current_file = open(input_file)

print "First let's print the whole file:\n"
#调用定义的函数，传了参数
print_all(current_file)

print "Now let's rewind,kind of like a tape"
#调用定义的函数，传了参数，使文件指针跳转到指定位置
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)
#rewind(current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)
#rewind(current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)


#加分题
#f.readline()写成了f.read()
'''
 python -m pydoc file
  seek(...)
 |      seek(offset[, whence]) -> None.  Move to new file position.
 

'''

