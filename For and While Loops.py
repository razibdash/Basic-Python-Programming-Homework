# Write a program that prints all numbers from 1 to 100. If the number is divisible by 3,
# print "Fizz", if divisible by 5, print "Buzz", and if divisible by both, print "FizzBuzz".

for i in range(1,101):
     print(i)
     if i%3==0 and i%5==0:
          print("FizzBuzz")
     elif i%5==0:
          print("Buzz")
     elif i%3==0:
          print("FIzz")
     else:
          print(i)

