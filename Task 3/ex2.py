# 1. Recursive Factorial
#    - Write a recursive function to calculate the factorial of a given number.
#    - Expected output: If the input is 5, the output should be "The factorial of 5 is 120."

a=int(input("Enter Input: "))

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    

print("The factorial of",a," is ",fact(a))