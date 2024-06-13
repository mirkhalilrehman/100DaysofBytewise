# 5. Guess the Number Game
#    - Write a program where the computer generates a random number, and the user has to guess it.
#    - Expected output: The program should prompt the user to enter a guess and 
# provide feedback on whether the guess is too high, too low, or correct.


import random

b=random.randint(1,100)
a=int(input('Enter number to guess:'))
if a<b:
    print('too low')
elif a>b:
    print('too high')
elif a==b:
    print('correct')