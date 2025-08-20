#Create a Python program that takes two numbers as input and outputs their sum,difference, multiplication, and division

num1=int(input())
num2=int(input())

def Sum(a,b):
     return a+b

def sub(a,b):
     return a-b
def mul(a,b):
      return a*b

def div(a,b):
     if a!=0:
          return a/b
     else:
          return "a is 0"

print(Sum(num1,num2))
print(sub(num1,num2))
print(mul(num1,num2))
print(div(num1,num2))