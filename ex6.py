# -- coding: utf-8 --
#给变量赋值，在字符串中留了个格式化字符，末尾赋值
x = "There are %d types of people." %10
#给变量赋值
binary = "binary"
do_not = "don't"
#给变量赋值，在字符串中留了两个格式化字符，末尾赋值
y = "Those who know %s and those who %s." %(binary,do_not)
#打印出下x,y变量的值
print x 
print y 
#打印出下x,y变量的值，使用%r格式化字符变量x,使用%s格式化字符变量y

print "I said: %r."%x
print "I also said: '%s'." %y

#bool变量，给hilarious赋值
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#拼接字符串，将hilarious转变为字符串
print joke_evaluation % hilarious
#给变量赋值
w = "This is the left side of ..."
e = "a string with a right side."
#拼接字符串，打印，+为字符串连接符
print w + e
