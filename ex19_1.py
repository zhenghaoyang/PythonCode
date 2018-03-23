# --coding: utf-8 --
#定义函数
from sys import argv 
script,from_file,to_file = argv
def study_python(how,why):
    print "how do you learn python %r \n" %how
    print "why you want to learn %r \n" %why
#1
study_python("through pratice python","it's funny")

#2
method = "pratice,code,think"
reason = "useful,simple,easy"
study_python(method,reason)
#3
study_python(method+"and just do it",reason+"most importance I like it")
#4
study_python(111,222)

method1 = " relax,slow"
reason1 = " earn money"
#5
study_python(method + method1,reason+reason1)
#6
study_python(raw_input(">"),raw_input("-->"))
#7
study_python(open(from_file).read(),open(to_file).read())
method=open('out.txt').read()
reason =open('out.txt').read()
#8
study_python(method+open('out.txt').read(),reason+open('out.txt').read())
#9
study_python(2+3,2+3)
#10
study_python(method+open('out.txt').read(),'111111')

#11
#study_python(method.read(),2+3)
#study_python(method.read(),111111)
'''  
study_python(method.read(),2+3)
AttributeError: 'str' object has no attribute 'read'
'''

