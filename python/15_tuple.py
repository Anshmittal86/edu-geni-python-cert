# Tuple:- Tuple is a collection of multiple value but it is Immutable.

seats = ("Rahul", "Ankit", "Priya") 
print(seats, type(seats), len(seats))

# Tuple can store different data types
train_info = ("Rajdhani", 12345, True)
print(train_info)

# Tuple allow duplicate values
seats = ("Rahul", "Ankit", "Rahul")
print(seats)

# Tuple is ordered (seat position remain fixed) 
seats = ("Rahul", "Ankit", "Priya")
print(seats)

# Creating Tuple without parentheses
seats = "Rahul", "Ankit", "Priya"
print(seats)

# Single element tuple needs comma
single_seat = ("Rahul",)
print(single_seat, type(single_seat))

# Access element using index (seat number)
seats = ("Rahul", "Ankit", "Priya")
print(seats[0]) # Rahul
print(seats[1]) # Ankit
print(seats[-1]) # Priya

# Slicing tuple (view some seats)
print(seats[0:2])

# Tuple is immutable (cannot change passenger directly)
seats[-1] = "Arjun" 
print(seats) # Error because tuple cannot be modified

# Tuple concatenation
coach1 = ("Rahul", "Ankit")
coach2 = ("Priya", "Anjali")
print(coach1 + coach2) # ('Rahul', 'Ankit', 'Priya', 'Anjali')

# Repetition repeats values
seat = ("VIP",) * 3
print(seat)

# Membership check 
print('Rahul' in ("Rahul", "Ankit", "Priya")) # True

# Tuple methods (only two because tuple is immutable)

t = (1, 2, 3, 4, 2)
print(t.count(2)) # 2
print(t.index(3)) # 4

# Packing values into tuple
passengers = "Rahul", "Ankit", "Priya"
print(passengers)

# Unpacking tuple values
a, b ,c = passengers 
print(a, c)

# Ignore values using underscore
a, _, c = passengers
print(a, c)

# Nested Tuple
train = ("coach1", ("Rahul", "Ankit"), "coach2", ("Priya", "Anjali"))
print(train[3][0]) # Priya

# convert string to tuple
letters = tuple("Train")
print(letters, len(letters)) # 5

