print("Developed by Pournima Ghanmode");

print("Demonstration of List");

def main():
	Continents = ["Asia", "Australia", "Europe", "North America", ];
	print(Continents)
	print(len(Continents))
	print(Continents[0])
	print(Continents[2:])
	print(Continents[:1])
	print(Continents[1:3])

	print("------------");

	data1 = ["C", "Java", "C++"]
	data2 = ["Python", "Angular", "PHP"]

	#comnines two different lists together
	combined = [data1, data2]
	print(combined)

	print("------------");

	#appends element in a list
	Continents.append("South America")
	print(Continents);

	#inserts element with desired index number
	Continents.insert(2,"Africa")
	print(Continents);

	#removes element
	Continents.remove("Australia")
	print(Continents);

	#deletes one element from right to left
	Continents.pop()
	print(Continents);

	#deletes element from given index number
	Continents.pop(2)
	print(Continents);

	#deletes elements from given index number onwards
	del Continents[1:]
	print(Continents);

	#adds elements
	Continents.extend(["Antarctica", "North America","Australia"])
	print(Continents);

	#sort the list elements alphabetically
	Continents.sort()
	print(Continents);

if __name__ == "__main__" :
	main();



