# functions:- function is a block of code which can reuse and we can run when it is called.

# syntax

# def function_name():
    # code

# function_name() # function calling

# simple function example

def greet():
    print("Welcome to the Movie Theater!")

greet()


# function with parameter

def greet_name(name):
    print(f'Welcome to the Theater {name}')

greet_name("Aman") 
greet_name("Rahul")

# function with return 

def calculate_ticket_price(tickets):
    total = tickets * 200
    return total

price = calculate_ticket_price(5)
print(f"Total price: {price}")

# function with default value

def calculate_ticket_price(tickets = 0):
    total = tickets * 200
    return total

price = calculate_ticket_price()
print(f"Total price: {price}")

# Arbitrary Arguments :- Used to store multiple Single value inside tuple (generally many developer use args as a name but you can use any name)
def total_sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

total_sum = total_sum(2, 3, 4, 5, 5, 6, 7, 8, 8, 8)
print(f"Total Sum: {total_sum}")


# Arbitrary Keyword Arguments :- Used to store multiple keyword value inside dictionary (generally many developer use kwargs as a name but you can use any name)

def greet_user(**kwargs):
    for key in kwargs:
        print(key)
        
    for value in kwargs.values():
        print(value)
    
    for key, value in kwargs.items():
        print(key, value)

greet_user(name="Ansh", age=12, gender="male")