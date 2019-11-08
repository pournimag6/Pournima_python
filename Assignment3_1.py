print("Addition of all the numbers from the list");

add = [];
total = int(input('Total numbers in the List: '));

for num in range(total):
    num = int(input('Enter number : '));
    add.append(num)

print("Sum of elements in given list is :", sum(add));