formatter = "%r %r %r %r"
print ("formatter % (1, 2,3,4)")
print (formatter % (3,4,5,6))

#print (formatter % ("one","two","three") 
#这样会出错：”格式字符串的参数不足”，应改为下面的：

print (formatter % ("one","two","three","four"))  
print (formatter % ('one','two','three','four'))

print (formatter % (formatter,formatter,formatter,formatter))	


#使用 argv 和raw_input 来从用户获取信息：

from sys import argv
script, filename = argv #前两行：使用argv获取文件名
txt = open(filename)  #使用open命令打开文件
print ("Here's your file %r:" % filename)
print (txt.read())
print ("Type the filename again:")
file_again = raw_input("> ")
txt_again = open(file_again)
print (txt_again.read())