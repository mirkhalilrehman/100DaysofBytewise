# Exercise: Simple Calculator
# Task: Write a program that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.

# Expected Output:
# Enter first number: 10
# Enter second number: 3
# Enter operation (+, -, *, /): /
# The result is: 3.3333333333333335

a=int(input("Enter First number: "))
b=int(input("Enter second number: "))
c=input("Enter operation(+,-,*,/): ")
if c=='+':
    print("The result is: ",a+b)
elif c=='-':
    print("The result is: ",a-b)
elif c=='*':
    print("The result is: ",a*b)
elif c=='/':
    print("The result is: ",a/b)
else:
    print('error occured')