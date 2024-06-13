# 6. List Comprehension
#    - Write a program that uses list comprehension to create a list of squares of the first 10 integers.
#    - Expected output: `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`

l=[i*i for i in range(1,11)]
print(l)