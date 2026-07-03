# Global Scope means a variable is accessible from anywhere in the program
name = "John"
print(name)

def print_name():
    print(name) # "John" because it is global scope variable

print_name()

# Local Scope means a variable is only accessible from within the function

def greet():
    name = "Ansh"
    print(name) # "Ansh" because it is local scope variable

print(name) # "John" because it is global scope variable
