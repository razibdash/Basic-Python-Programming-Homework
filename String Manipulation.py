# Create a Python program that takes a string input and prints it in reverse.
#  Write a function to check whether a given string is a palindrome.

str1=input()

def revFunc(s):
     ans=''
     for i in range(len(s)-1,-1,-1):
          ans+=s[i]
    
     return ans

print(revFunc(str1))