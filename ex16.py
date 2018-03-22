# --coding: utf-8 --
#从sys模块导入argv参数
from sys import argv
#argv接受两个参数
srcipt,filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C(^C)."
print "If you do want that,hit RETURN."

raw_input("?")
print "Open the file..."
#以可写的方式打开文件
target = open(filename,'w')
print "Truncate the file. Goodbye"
#truncate() 方法用于从文件的首行首字符开始截断，截断文件为 size 个字符
#size -- 可选，如果存在则文件截断为 size 字节。
target.truncate()
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1 :")
line2 = raw_input("line 2 :")
line3 = raw_input("line 3 :")

print "I'm going to write these to the file."

target.write("first line"+line1+"\n"+"two line"+line2+"\n"+"three line"+line3+"\n")
'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
print "And finally,we close it."
target.close()


#加分题
#没有指定W模式
#IOError: File not open for writing
