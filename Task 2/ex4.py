# 4. Prime Number Checker
#    - Write a program to check if a given number is prime.
#    - Expected output: If the input is 7, the output should be "7 is a prime number." If the input is 10, the output should be "10 is not a prime number."
import math

n = int(input("Enter number "))

if n <= 1:
    print(n, 'is not prime')
elif n == 2:
    print(n, 'is prime')
elif n % 2 == 0:
    print(n, 'is not prime')
else:
    is_prime = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, 'is prime')
    else:
        print(n, 'is not prime')
