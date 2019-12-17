print("Devloped by Pournima Ghanmode")
print("Demonstration of Data types");

def main():

	#None datatype
	no = None
	print(no);
	print(type(no))
	print(id(no))
	print("------------");

	#Numeric datatype
	#Numeric datatype contains different sub types i.e int, float, boolean, complex
	no = 11; #int
	print(no);
	print(type(no))
	print("------------");

	no = 3.14; #float
	print(no);
	print(type(no))
	print("------------");

	no = True; #boolean
	print(no);
	print(type(no))
	print("------------");

	no = 3+14j; #complex
	print(no);
	print(type(no))
	print("------------");

	#we can type cast one data into another datatype
	no = 18.7
	no = int(no)
	print(no)
	print(type(no))
	print("------------");

	a = 5
	b = 6
	no = complex(a,b)
	print(no)
	print(type(no))
	print(id(no))
	print("------------");

	#Sequence datatype contains different types of datatypes i.e List, Set, Tuple, Range
	Listex = [10, 20 ,30 ,40, 50] #List datatype
	print(Listex)
	print(type(Listex))
	print("------------");

	Setex = {"Asia", "Australia", "Europe", "Africa", "North America", "South America", "Antarctica"} #Set datatype
	print(Setex)
	print(type(Setex))
	print("------------");

	Tupex = ("Asia", "Australia", "Europe", "Africa", "North America", "South America", "Antarctica") #Tuple datatype
	print(Tupex)
	print(type(Tupex))
	print("------------");

	Rangex = list(range(1,10)) #Range datatype
	print(Rangex)
	print(type(Rangex))
	print("------------");

	Rangex = list(range(15)) #Range datatype
	print(Rangex)
	print(type(Rangex))
	print("------------");

	Rangex = list(range(1,50,5)) #Range datatype
	print(Rangex)
	print(type(Rangex))
	print("------------");

	#Dictionary datatype contains key and value

	Continents = {"English" : "75", "Science" : "88", "Social Science" : "82", "Sanskrit" : "90"}
	print(Continents)
	print(type(Continents))
	print(Continents.keys())
	print(Continents.values())
	print(Continents["Science"])


if __name__ == "__main__" :
	main();

























