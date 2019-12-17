print("Developed by Pournima Ghanmode");

print("Demonstration of Array");

import array as arr

def main():

	a = arr.array('i', [2,4,6,8])
	print("First element : ",a[0])
	print("second element : ",a[1])
	print("second last element : ",a[-1])
	print(a.typecode);

	print("------------");

	c = arr.array('f', [2.4,4.5,6.1,8.75])
	print("First element : ",c[0])
	print("second element : ",c[1])
	print("second last element : ",c[-1])
	print(c.typecode);

	print("------------");

	a.reverse()
	for i in range(len(a)):
		print(a[i])

	print("------------");

	b = arr.array('i',[4,8,10,24])
	for i in range(len(b)):
		print(b[i])

	print("------------");

	i=0
	while(i<len(b)):
		print(b[i])
		i+=1

if __name__ == "__main__" :
	main();