print("Addition of digits");

n = int(input("Enter a number:"));

sum = 0;

while(n>0):
    x = n % 10
    sum = sum + x
    n = n // 10

print("Addition of digits is:",sum);