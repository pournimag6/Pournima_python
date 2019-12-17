print("Developed by Pournima Ghanmode");

print("Demonstration of Tuples")

def main():
	tup = (11, "Butter", "Bread", 25.6, 90, "Salt");
	print(tup);
	print(tup[0]);
	print(tup[3]);
	print(tup[2:]);
	print(tup[:4]);
	print(tup[2:4]);
	print(len(tup));
	print("Butter" in tup);
	del tup



if __name__ == "__main__" :
	main();