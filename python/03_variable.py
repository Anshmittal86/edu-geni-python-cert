# Variable:- Variable is like a container which can store a value so that we can use later in the code.

# note:- Variable are stored in object in the python

name = input("Enter your name: ")
print("Your name is " + name)


# Your name is ----- and you order ----.
name = input("Enter your name: ")
food = input("Enter your order: ")
print("Your name is " + name + " and you order " + food + ".")
print(f"Your name is {name} and you order {food}.")


# Task:- Take name and age from the user and print it.
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Your name is {name} and you are {age} year old.")

# Multiple Assignment
# a = 1
# b = 2
# c = 3
a, b, c = 1, 2, 3

# Same Value to multiple Variable
a = b = c = 1


# Variable Naming Rules:

# 1. Variable can only contain Alphabets(a-zA-Z), Digits (0-9) and underscore(_)
# 2. Variable can't include digits at the start of the variable
# 3. Variable are case sensitive 
# 4. Variable can't include the keywords.(if, we, while, do while etc.)