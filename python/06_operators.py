# Operator:- Operator is used to perform some operation on the Operands for example:- Arithmetic, Logical etc.

# - Operands :- Value which we perform the operation

# Arithmetic 

# Addition
print(2 + 2) # 4 

# Subtraction
print(2 - 2) # 0

# Multiply
print(2 * 2) # 4

# Divide
print(5 / 2) # 2.5

# Floor Division
print(5 // 2) # 2 

# Modulus
print(5 % 2) # 1

# Power Operator
print(2 ** 3) # 8



# Assignment Operator

a = 10

a += 5      # a = a + 5
a -= 5      # a = a - 5
a *= 5      # a = a * 5
a /= 5      # a = a / 5
a //= 5     # a = a // 5
a %= 5      # a = a % 5
a **= 5     # a = a ** 5

# Comparison Operator

# Equal == 
print(2 == 2) # True

# Not Equal
print(5 != 3) # True

# Greater than
print(5 > 2) # True

# less than
print(5 < 2) # False

# Greater than or equal to
print(5 >= 2) # True

# Less than or equal to
print(5 <= 2) # True



# Logical Operator

# and
print(5 > 2 and 4 < 1) # False

# or
print(5 > 2 or 4 < 1) # True

# not
print(not(5 > 2 or 4 < 1)) # False


# Identity Operator

# is : True if both object are save in the same memory location
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

print(list1 is list2) # False

# is not :- True if both object are not save in the same memory location
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
 
print(list1 is not list2) # True

# Membership Operator

# in 
movie = "Iron Man"
favorite_movies = ["Avengers", "Iron Man", "Batman"]
print(movie in favorite_movies) # True

# not in
movie="Black Panther"
favorite_movies = ["Avengers", "Iron Man", "Batman"]
print(movie not in favorite_movies) # True