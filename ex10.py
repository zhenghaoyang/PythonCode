# --coding: utf-8 --
tabby_cat = "\tI'm tabbed in. \n%r\t"
persian_cat = "I'm split\non a line."
backslash_cat = "\t\t\t\nI'm \\a \\cat."
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''
#
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
male = True;
print tabby_cat % male

#%r 打印出来的是你写在脚本里的内容,转义序列无效，
#而 %s 打印的是你应该看到的内容，转义序列有效
print "I want a cat that is %r"%backslash_cat
print "I want a cat that is %s"%backslash_cat
print "I'm\tso\nhappy so I \'%r\'."%tabby_cat % male
print "I'm\tso\nhappy so I \'%s\'."%tabby_cat % male



