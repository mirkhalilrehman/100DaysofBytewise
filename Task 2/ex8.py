# 8. Anagram Checker
#    - Write a program to check if two strings are anagrams (contain the 
# same characters in a different order).
#    - Expected output: If the two strings are "listen" and "silent", 
# the output should be "listen and silent are anagrams."
#  If the two strings are "python" and "java", the output should be
#  "python and java are not anagrams."

aa=input('Enter string 1:')
bb=input('Enter string 2:')

a=[i.lower() for i in aa]
b=[i.lower() for i in bb]
a=sorted(a)
b=sorted(b)
# print(a,b)
if a==b:
    print(aa,' , ',bb,' are anagrams')
else:
    print(aa,' , ',bb,' are not anagrams')
