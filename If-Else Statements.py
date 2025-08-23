# Write a Python program that asks for the user’s age and checks if they are eligible to vote
# (18 years and above). Print an appropriate message based on the age input
def checkAge(age):
    if age<=18:
        return f"your age: {age} not eligible to vote"
    else:
        return f"your age: {age} so eligible to vote"

age=int(input("enter age: "))

print(checkAge(age))