# Exercise: Check for Palindrome
# Task: Write a program to check if a given string is a palindrome.

# Expected Output:
# Enter a string: radar
# radar is a palindrome

n=input('Enter a string:')
if n==n[::-1]:
    print(n,' is palindrome')
else:
    print(n,' is not palindrome')
