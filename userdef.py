print("Developed by Pournima Ghanmode")

print("Demonstration of Advanced functions")


#function which accepts nothing and returns nothing

def fun1():
	print("Inside fun1");

#function which accepts value and returns nothing

def fun2(value):
	print("Inside fun2");
	print("Accepted value is", value)

#function which accepts value and returns value

def fun3(value):
	print("Inside fun3");
	print("Accepted value is", value)
	return value+1

#function which accepts multiple values and returns multiple values

def fun4(value1,value2):
	print("Inside fun4")
	add = value1 + value2
	sub = value1 - value2
	return add,sub

#function which calls another function which is defined outside it

def fun5():
	print("Inside fun5")
	fun1();

#function which contains another nested function defined in it
def fun6():
	print("Inside fun6")
	def Innerfun():
		print("Inside Inner fun");
	Innerfun()

#all function calls
value = 10;
fun1();
print("---------------------------------------");

fun2(value);
print("---------------------------------------");

ret = fun3(value);
print("return value", ret)
print("---------------------------------------");

ret1,ret2 = fun4(10,4)
print("addition is", ret1)
print("subtraction is", ret2)
print("---------------------------------------");

fun5();
print("---------------------------------------");

fun6();



















