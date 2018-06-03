# 使用关键参数：
def func(a ,b=5, c=10 ):
	print("'a is',a,'and b is',b,'and c is',c")
	func(3, 7)
	func(25, c=24)
	func(c=50, a=100)

def maximum(x, y):
	if x > y:
		return x
	else:
		return y
		print ("maximum(3, 4)")	