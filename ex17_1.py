# --coding: utf-8 --
#从sys模块导入argv参数
from sys import argv 
from os.path import exists
script,from_file,to_file = argv
print "copying from %s to %s" %(from_file,to_file)

#input = open(from_file)
'''
indata = open(from_file).read()
output = open(to_file,'w')
output.write(open(from_file).read())
'''
open(to_file,'w').write(open(from_file).read())


print "Alright,all done."




#加分题

