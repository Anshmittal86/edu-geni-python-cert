# String is a sequence of characters which is enclosed in single quotes or double quotes or triple quotes.
# String is a immutable data type.

movie = "Avengers"
city = 'Mumbai'
review = """This movie is 
full of action"""
print(movie, city, review)

# Accessing character using index (start from 0)
print(movie[0])


# Negative Indexing starts from the last character (start from -1) 
print(movie[-1])


# print(movie[start:end:step])
print(movie[2:5:2])
print(movie[:4])    # always start from 0 
print(movie[0:])    # always end to -1 
print(movie[:])     # always return a new copy 

# print(movie[start:end:step])
print(movie[-4:-1])
print(movie[:-1])   # always start from 0
print(movie[-4:])   # always end to -1 
print(movie[:])     # always return a new copy 


# string concatenation join two or more string
hero = "Tony Stark"
movie = "Iron Man"

print(movie + " movie's hero name is " + hero + ".")
print(f"{movie} movie's hero name is {hero}.")


# Loop through each character of a string
for char in hero:
    print(char)
    

# Check if text exists inside a string
title = "Avengers Endgame"
isAvailable = "Avengers" in title
print(isAvailable) # True

title = "Avengers Endgame"
isNotAvailable = "Avengers" not in title
print(isNotAvailable) # False


# len() :- Get total number of character
movie = "Avatar"
print(len(movie))

# strip:- remove left and right unwanted space
movie = "   Avatar is a good movie   "
print(movie.strip())

# upper() :- Convert string to uppercase
name = 'Avatar is good movie'
print(name.upper())

# lower() :- Convert string to lowercase
print(name.lower())

# capitalize() :- Convert first letter to uppercase
print(name.capitalize())

# title():- Convert first letter of the word to uppercase
print(name.title())

# replace(old, new)
print(name.replace("is", "was"))
print(name) 

# split string into list
data = 'Action Drama SciFi'
print(data.split())

# Join list into string
msgList = ["Interstellar", "is", "amazing"]
msg = " ".join(msgList)
print(msg) 

# count() :- count method count the number of times a substring occurs in a string
msg = "Interstellar is amazing"
print(msg.count("e")) # 2

# find():- find method returns the index of the first occurrence of a substring in a string if value is not found then it will return -1
print(msg.find("is")) # 13

# index() :- index method returns the index of the first occurrence of a substring in a string if value is not found then it will raise an error
print(msg.index("is")) # 13


# startswith() :- returns True if the string starts with the specified value
print(msg.startswith("Interstellar")) # True

# endswith() :- returns True if the string ends with the specified value
print(msg.endswith("amazing")) # True


# Escape Sequences
# \n :- new line
# \t :- tab
# \\ :- backslash
# \' :- single quote
# \" :- double quote

print("Ansh\nMittal")
print('Ansh\'Mittal')
print("Ansh\"Mittal")