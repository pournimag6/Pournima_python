print("Sum of digits using recursion");

arr = []

def summation(x):
    if(x==0):
        return arr
    digit = x%10
    arr.append(digit)
    summation(x//10)
n = int(input("Enter a number: "))
summation(n)
print(sum(arr))