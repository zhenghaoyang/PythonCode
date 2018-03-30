# --coding: utf-8 --
#每一个习题的脚本里，把你碰到的每一个词和每一个符号
print()	打印内容到屏幕上
raw_input()	接受用户输入内容
import	加载其他的库、类或函数到当前脚本
return	返回函数的结果
pydoc	在命令行查看某个函数或类的帮助文档
help	查看类、函数、变量的帮助文档
def	用于定义一个函数
Ture	布尔值“真”，首字母大写
False	布尔值“假”，首字母大写
sys	标准库，和环境有关的功能
sys.argv	属于sys标准库，获取脚本参数
open	用于打开文件，注意打开后的对象和 py2 file 的区别
TextIOWrapper	Py3 打开文本文件后的类型
TextIOWrapper.read	从当前指针位置读取文件的内容
TextIOWrapper.readline	从指针位置读取文件内容
TextIOWrapper.writer	向文件写入内容
TextIOWrapper.close	关闭打开的文件，执行保存
TextIOWrapper.seek	设置文件指针位置
TextIOWrapper.tell	返回当前指针位置
os	标准库，和系统操作有关
os.path	属于 os 库，和路径有关的操作
os.path.exists	判断文件是否已经存在
字符串	由引号（' " ''' """）定义的一组字符
原始字符串	字符串的引号前有字母r 或 R，其内容不会被转义。
转义字符	由 \ 和一些字符组成，被转义的字符表示特殊的意义
整数	表示没有小数的数字
浮点数	表示有小数部分的数字，浮点数运算时可能出现精度问题。
科学计数法	由数字和e组成，表示数字乘以10的多少次方
+	加法运算 或拼接字符串
-	减法运算
*	乘法运算
**	幂运算
/	除法运算，结果一定是浮点数
//	整除或地板除，其结果舍弃小数部分
%	取余
=	赋值
+=	相加后赋值
-=	相减后赋值
*=	相乘后赋值
/=	相除后赋值
//=	整除后赋值
%=	取余后赋值
==	判断是否相等
<	判断是否小于
>	判断是否大于
>=	判断是否小于等于
<=	判断是否大于等于
!=	判断是否不等于
\n	转义字符，换行
\\	转义字符，\
\’ 和 \”	转义字符，引号
\ （行末）	转义字符，不换行
\t	转义字符，横向制表符
\v	转义字符，纵向制表符
\a	转义字符，响铃
\b	转义字符，退格（后面字符前移）
\000	转义字符，表示空（但不是空格）
\r	转义字符，回车（效果类似 \b 但光标是移动到首行后输出后面的字符）
\f	转义字符，换页(据说在有些终端会清空屏幕）
\ooo	转义字符，八进字符，ooo代表的字符的值，例如：\044是美元符$
\xhh	转义字符，十六进制字符，hh代表的字符的值，例如：\x44是大写D
%s	格式化字符，字符串
%r	格式化字符，原始字符
%d	格式化字符，整数
%f	格式化字符，浮点数
%c	格式化字符，转换为字符
%o	格式化字符，8进制整数
%x, %X	格式化字符，16进制整数
%e, %E	格式化字符，科学计数法表示浮点数
%g， %G	格式化字符，10 进制或科学计数法表示浮点数
*	辅助格式化字符，定义宽度或浮点位数
m.n	辅助格式化字符，m定义宽度，n定义浮点位数
-	辅助格式化字符，左对齐
+	辅助格式化字符，正数显示正号
#	辅助格式化字符，在 8、 16 进制数前显示进制符号（8进制：0o123; 16进制：0x123 或 0X123)
0	辅助格式化字符，位数不足宽度时用 0 填充而非空格。
(var)	辅助格式化字符，映射变量（通常用来处理字段类型的参数）

1.print 
2.#
3.print "",+/
4.%s,%#print "Let's talk about %s."%my_name
5.%(,)#print "He's got %s eyes and %s hair."%(my_eyes,my_hair)
6.%(,,++)
#print "If I Add %d,%d,and %d I get %d."%(age,height,weight,age+height+weight)
7.x="%d",%10#x = "There are %d types of people." %10
8.hilarious = False
9.print joke_evaluation % hilarious
10.print w + e
11."%s",%'snow'#print "Its fleece was white as %s." %'snow'
12.""*10#print "." *10#What'd that do?
13.formatter = "%r %r %r %r"#print formatter %(1,2,3,4)
14./n,#months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
15.""""""#"""长字符串"""
16.\t制表符#tabby_cat = "\tI'm tabbed in. \n%r\t"
17.#%r 转义序列无效
18.raw_input()，raw_input("input:")
19.from sys import argv
   script,first,second,third = argv
20.多个参数
 print """
Alright, so you said %s about liking me.
You live in %s.Not sure where that is.
And you have a %s computer.
You use %s System,But you like %s
Nice.
"""%(likes,lives,computer,useSystem,likeSystem)
21.txt = open(filename)
txt.read()
txt.close()
22.target = open(filename,'w')
target.truncate()
23.
output.write(indata)
24.def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r,arg2: %r"%(arg1,arg2)
25.
#变量计算后，传参
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers +1000)



 

#列表做好以后，再花几天时间重写一遍这份列表，确认里边的东西都是正确的

#记住了这份列表中的所有内容，就试着把这份列表默写一遍

#发现自己漏掉或者忘记了某些内容，就回去再记一遍

#知道它的意义很重要。它会让你明确目标，让你知道你所有努力的目的

#
