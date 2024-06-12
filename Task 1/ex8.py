# Exercise : Fibonacci Sequence
# Task: Write a program to print the Fibonacci sequence up to n terms.

# Expected Output:
# How many terms? 5
# Fibonacci sequence:
# 0 1 1 2 3 

n=int(input("How many terms? "))

n1,n2=0,1
count=0
if n==1:
    print(n1)
else:
    while(count<n): 
        print(n1,end=" ") 
        nn=n1+n2
        n1=n2
        n2=nn
        count+=1 
    
    
