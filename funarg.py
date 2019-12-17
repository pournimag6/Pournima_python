print("Developed by Pournima Ghanmode")

print("Demonstration of function arguments")

#Position arguments
def Marks(Subject, Score) :
	print("Subject is", Subject);
	print("Score is", Score);
print("---------------------------------------");
print("Demonstration of Position arguments")
Marks("English", 92) 
Marks("Science", 90)

#Keyword arguments
def Batches(name, fees) :
	print("Batchname  is", name);
	print("fee is", fees);
print("---------------------------------------");
print("Demonstration of Keyword arguments")	
Batches(name="Python", fees=9000)
Batches(fees=5000, name="Angular")

#Default arguments
def Batches1(name, fees=5500) :
	print("Batchname  is", name);
	print("fee is", fees);
print("---------------------------------------");
print("Demonstration of Default arguments")	
Batches1(name="Python", fees=9000)
Batches1(name="Angular")
Batches1(fees=5000, name="C Language")

#Variable no. of arguments
def Add(*no):
	ans = 0
	for i in no:
		ans = ans + i
	return ans
print("---------------------------------------");
print("Demonstration of Variable number of Arguments")
ret = Add(10,20,30)
print("Addition is ",ret)
ret = Add(10,20,30,40,50,60)
print("Addition is ",ret)
ret = Add(10,20)
print("Addition is ",ret)

#Keyword variable no. of arguments
def StudentInfo(**other) :
	print(other)
	for i,j in other.items() :
		print(i,j)
print("---------------------------------------");
print("Demonstration Keyword variable no. of arguments")
StudentInfo(name = "XYZ", age = 23, address = "Pune", mobile = 1234567890)







