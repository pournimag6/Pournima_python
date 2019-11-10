print("Displaying pattern using recursion");

i = 1

def fun():
	global i
	if(i<=5):
		print(i, end=" ")
		i=i+1
		fun()
fun()