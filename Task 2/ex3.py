# 3. Nth Fibonacci Number

# • Write a program to find the nth Fibonacci number.
# • Expected output: If the input is 10, the output should be "The 10th Fibonacci number is 55.”

n=int(input("which term "))

n1,n2=0,1
count=0
if n==1:
    print(n1)
else:
    while(count<n): 
        nn=n1+n2
        n1=n2
        n2=nn
        count+=1 
    print('term Fibonacci nimber is',n1)      
    
    