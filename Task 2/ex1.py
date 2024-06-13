# 1. Palindrome Checker (Word)

# • Write a program to check if a given word is a palindrome (reads the same forwards and backwards).
# • Expected output: If the input is "racecar", the output should be "racecar is a palindrome." If the input is "Python", the output should be "Python is not a palindrome.”

n=input("Enter String:")
if n==n[::-1]:
    print(n," is palindrome")
else:
     print(n," is not palindrome")