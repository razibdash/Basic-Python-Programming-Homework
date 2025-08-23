# Create a Python program that takes a string input and prints it in reverse.


str1=input()

def revFunc(s):
     ans=''
     for i in range(len(s)-1,-1,-1):
          ans+=s[i]
    
     return ans

print(revFunc(str1))

# Write a function to check whether a given string is a palindrome.
 
str2=input()

if str2 == revFunc(str2):
     print("palindrome")
else:
     print("Not palindrome")
