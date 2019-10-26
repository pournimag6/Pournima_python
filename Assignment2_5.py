print("To check whether number is prime or not");

no = int(input("enter a number: "))
 
for i in range(2, no):
	if no % i  == 0:
		print("not prime number")
		break
else:
	print("prime number")