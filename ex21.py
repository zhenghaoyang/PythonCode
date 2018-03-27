# --coding: utf-8 --
def add(a,b):
    print "ADDING %d + %d"%(a,b)
    return a+b
def subtract(a,b):
    print "SUBTRACTING %d - %d" %(a,b)
    return a - b
def mutiply(a,b):
    print "MUTIPLYING %d * %d"%(a,b)
    return a * b;
def divide(a,b):
    print "DIVDING %d / %d" %(a,b)
    return a/b
print "Let's do some math with just functions!"

age = add(30,5)
heigth = subtract(78,4)
weight =  mutiply(90,2)
iq = divide(100,2)

print "Age : %d,Height:%d,Weight:%d,IQ:%d"%(age,heigth,weight,iq)
what = add(age,subtract(heigth,mutiply(weight,divide(iq,2))))
print "Here is a puzzle"

print "That becomes:",what,"Can you do it by hand?"

what = divide(iq,2)

what = mutiply(weight,what)

what = subtract(height,what)

add(age,what)

print "That becomes:",what
#加分习题
