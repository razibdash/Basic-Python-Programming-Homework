# Write a Python function that takes two numbers as arguments and returns their multiplication.

def multi(a,b):
    return f"multiplication :{a*b}"

print(multi(2,2))

# Implement a function to check if a number is prime or not.

def checkPrime(n):
    if n <= 1:   # 0, 1, and negative numbers are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True


num = 29
if checkPrime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
