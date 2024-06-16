# 3. Merge Sorted Arrays
#    - Write a function that takes two sorted arrays and merges them into a single sorted array.
#    - Expected output: If the two input arrays are `[1, 3, 5]` and `[2, 4, 6]`, the output should be 
# `[1, 2, 3, 4, 5, 6]`.

a=[1, 3, 5]
b=[2, 4, 6]

c=a+b
c=sorted(c)
print(c)