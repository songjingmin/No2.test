def  printMax(a,b):
	if a > b :
		print("a,'is maximum'")
	else:
		print("b,'is maximum'")
printMax(3,4)
x = 5
y = 7
printMax(x,y)


def func(x):
    print ("'x is', x")
    x = 2
    print ("'Changed local x to', x")

x = 50
func(x)
print ("'x is still', x")



#使用global语句
def func():
    global x

    print ("'x is', x")
    x = 2
    print ("'Changed local x to', x")

x = 50
func()
print ("'Value of x is', x")