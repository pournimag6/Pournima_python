print("Maximum number from the list");

arr = [];

num = int(input('How many numbers: '));

for n in range(num):
    numbers = int(input('Enter number '))
    arr.append(numbers)

print("\nMaximum element in the list is :", max(arr));