# Exercise: Count Vowels
# Task: Write a program that counts the number of vowels in a given string.

# Expected Output:
# Enter a string: Nimra Waqar
# The number of vowels is: 4

n=input("Enter a string:")
c=0
v=['a','e','i','o','u']
for i in n:
    if i in v:
        c=c+1

print("Total vowels in ",n,' are :',c)