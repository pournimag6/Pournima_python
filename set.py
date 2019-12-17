print("Developed by Pournima Ghanmode");

print("Demonstration of Set");

def main():

	Container = {6, "Kunda", 3.14, "Java", 20}

	print(Container);
	print(len(Container))
	Container.remove("Java")
	print(Container)
	Container.discard(20)
	Container.add("Peacock")
	Container.add("Parrot")
	Container.add("Panda")
	print(Container)
	print(len(Container))



if __name__ == "__main__" :
	main();