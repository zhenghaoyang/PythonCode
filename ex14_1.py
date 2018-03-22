# --coding: utf-8 --
from sys import argv
script,user_name,useSystem = argv 
prompt = '--------------->'
print "Hi %s,I'm the %s script run on %s." %(user_name,script,useSystem)
print "I'd like to ask you a few question."
print "Do you like me %s" %user_name

likes = raw_input(prompt)

print "Where do you live %s" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print "You use what %s System,you like what kind of System?"%useSystem
likeSystem = raw_input(prompt)


print """
Alright, so you said %s about liking me.
You live in %s.Not sure where that is.
And you have a %s computer.
You use %s System,But you like %s
Nice.
"""%(likes,lives,computer,useSystem,likeSystem)
