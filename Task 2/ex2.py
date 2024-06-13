# 2. FizzBuzz
#    - Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz" 
# instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of
#  both 3 and 5, print "FizzBuzz".
#    - Expected output:
#      1
#      2
#      Fizz
#      4
#      Buzz
#      Fizz
#      7
#      8
#      Fizz
#      Buzz
#      11
#      Fizz
#      13
#      14
#      FizzBuzz

for i in range(1,101):
    if(i%3==0 and i%5==0):
        print('FizzBuzz')
    elif(i%5==0):
        print('Buzz')
    elif(i%3==0):
        print('Fizz')
    else:
        print(i)
