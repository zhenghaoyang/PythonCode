# --coding: utf-8 --
print "How old are you?",
age = raw_input()
print "How tall are you?",

height = raw_input()

print "How much do you weigh?",

weight = raw_input()

print "Which book do you like most?",
book = raw_input("input:")

type(book)
#单引号需要被转义，从而防止它被识别为字符串的结尾。
#How old are you? 11'11"
#How tall are you? 11"11"
#How much do you weigh? 11"11'
#Which book do you like most? input:'11"11"
print "So you're %r old ,%r tall and %r heavy,you like this %s book"%(age,height,weight,book)



