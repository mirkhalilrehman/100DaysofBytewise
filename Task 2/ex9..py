# 9. Reverse Words in a Sentence
#    - Write a program to reverse the order of words in a given sentence.
#    - Expected output: If the input sentence is "The quick brown fox jumps over the lazy dog.",
#  the output should be "dog. lazy the over jumps fox brown quick The"

a=input('Enter string :')
b=a.split(' ')
b=b[::-1]
c=' '.join(b)
print(c)
