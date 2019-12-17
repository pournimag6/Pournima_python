print("Developed by Pournima Ghanmode");

print("Demonstration of String");

def main():
	name = "Australia"
	newname = 'Australia'

	print(name);
	print(type(name));
	print(newname);
	print(type(newname))

	print(name[0]);
	print(name[8]);

	print(name[-1]);

	print(name[:3]);

	print(len(name))

	className = " Pournima Naresh Ghanmode "
	print(className.strip())

	Fruits = "Mango, Banana, Kiwi, Watermelon, Pineapple"
	print(Fruits.split(","))

if __name__ == "__main__" :
	main();