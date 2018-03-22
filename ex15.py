# --coding: utf-8 --
#从sys模块导入argv
from sys import argv
#用户输入参数解包
script,filename = argv
#打开文件，赋值给txt
txt = open(filename)
#打印出文件名
print "Here's your file %r:"%filename
#打印出txt变量读取文件的文本
#txt.close()
print txt.read()
txt.close()
print "Type the filename again:"
#读取用户输入的参数
file_again = raw_input(">")
#读取用户输入的文件名，读取其中的文本，赋值给txt_again
txt_again = open(file_again)
#打印出txt_again读取到的文本
print txt_again.read()

txt_again.close()


#加分题
#与类和实例无绑定关系的function都属于函数（function）；
#与类和实例有绑定关系的function都属于方法（method）。
"""print "Type the filename again:"
#读取用户输入的参数
file_again = raw_input(">")
#读取用户输入的文件名，读取其中的文本，赋值给txt_again
txt_again = open(file_again)
#打印出txt_again读取到的文本
print txt_again.read() """
#只是用  raw_input 写这个脚本，想想那种得到文件名称的方法更好，以及为什么。
#raw_input，可拓展行好
'''
>>> txt = open('D:\PythonCode\ex15_sample.txt')
>>> txt.read()
'This is stuff I typed into a file.\nIt is really cool stuff.\nLots and lots of fun to have in here.'
'''

