# --coding: utf-8 --
#定义函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheese!" %cheese_count
    print "You have %d boxes of cracker!" %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly:"
#直接传参
cheese_and_crackers(20,30)

print "OR,We can use variables from our script:"

#给变量赋值
amount_of_cheese = 10
amount_of_crackers = 50

#用变量传参
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"

#计算完直接传参
cheese_and_crackers(10+20,5+6)

print "And we combine the two,variables and math:"

#变量计算后，传参
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers +1000)

#加分题

