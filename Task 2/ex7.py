# 7. Palindrome Sentences
#    - Write a program to check if a given sentence is a palindrome (reads the same forwards and backwards, ignoring spaces and punctuation).
#    - Expected output: If the input is "A man, a plan, a canal: Panama", the output should be 
# "A man, a plan, a canal: Panama is a palindrome." If the input is "Hello, world!", 
# the output should be "Hello, world! is not a palindrome."

n=input("Enter String:")
nn=n
nn=nn.replace(' ','').replace(',','').replace(':','').lower()

if nn==nn[::-1]:
    print(n," is palindrome")
else:
     print(n," is not palindrome")
