from functools import *;

def AcceptData():
	size = int(input("Enter number of elements"));
	arr= list();
	print("Enter the elements");

	for i in range(0,size,1):
		print("Enter number",i + 1)
		no = int(input());
		arr.append(no);
	return arr;

def main():
	RawData = AcceptData();
	print("Accepted data is ");
	print(RawData);

	FilteredData = list(filter(lambda no:(70<no<=90),RawData));
	print("Filtered data is");
	print(FilteredData);

	ModifiedData = list(map(lambda no:no+10,FilteredData));
	print("Modified data is ");
	print(ModifiedData);

	if(len(ModifiedData) > 0):
		result = reduce(lambda no1,no2:(no1*no2),ModifiedData);
		print("Final result is",result);
	else:
		print("There is no result");

if __name__ == "__main__":
	main();