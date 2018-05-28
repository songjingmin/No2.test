days = "Mon Tue Wed Thu Fri Sat Sun"	
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print ("Here are the days:",days)
print("Here are the months:",months)		
print (""" 
There is something going on here.
with the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")	
#当字符串使用%r 时\n显示新行就没用了：打印出的是你写出来的方式(或者近似方式)
print ("Here are the %r" %months)
#正确写法：
print ("I am 6'2\" tall.") #将字符串中的双引号转义,本意指寸

print('I am 6\'2" tall.')# 将字符串中的单引号转义，本意指尺

#错误写法：不将双引号转义会报错
print ("I am 6'2" tall.")	