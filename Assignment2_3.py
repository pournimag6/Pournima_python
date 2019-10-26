print("Factorial of given number");

def factorial(no):
    if no == 1:
        return no;
    else:
        return no * factorial(no - 1);

no = int(input("Enter a Number: "))

if no < 0:
    print("Factorial can't be found for negative numbers");
elif no == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", no, "is: ", factorial(no));

