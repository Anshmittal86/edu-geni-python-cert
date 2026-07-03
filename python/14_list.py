# List :- List is a collection to store multiple value
movies = ["Avengers", "Iron Man", "Batman"]
print(movies)

# List can store different data types
mixed_List = ["Avatar", 2009, 8.7, True]
print(mixed_List)

# List are ordered, items stay in the same order
movies = ["Avengers", "Iron Man", "Batman"]
print(movies)

# List allow duplicate values
movies = ["Avengers", "Batman", "Batman"]
print(movies)

# List are mutable (List can be changed)
movies = ["Avengers", "Batman", "Batman"]
movies[1] = "Antman"
print(movies)

newMovies = movies[:]
newMovies[0:3] = ["Avengers", "Iron Man"] # Not Recommended
print(newMovies) # ["Iron Man", "Black Panther", "Batman"]

# Accessing elements using index (index starts form 0)
movies = ["Avengers", "Batman", "Batman"]
print(movies[1])
print(movies[-1])

# List slicing extracts part of the list
# print(movies[start:end:step])
print(movies[0:3])
print(movies[:2])   # always start from 0
print(movies[1:])   # always end to -1 
print(movies[:])    # always return a new copy 

print(movies[-4:-1])
print(movies[:-1])  # always start from 0
print(movies[-4:])  # always end to -1 
print(movies[:])    # always return a new copy 

# List methods

# append():- adds item at the end
movies = ["Avengers", "Batman"]
movies.append("Joker")
print(movies)

# insert():- adds item at a specific position
movies = ["Avengers", "Batman"]
movies.insert(1, "Joker")
# movies.insert(-1, "Joker")
print(movies)

# pop():- removes item using index if not found then return the error
movies = ["Avengers", "Batman", "Batman"]
movies.pop(1)
print(movies)

# remove():- removes first occurrence of item if not found then return the error
movies = ["Avengers", "Batman", "Batman"]
movies.remove("Batman")
print(movies) # ["Avengers", "Batman"]

# clear():- removes all the items
movies = ["Avengers", "Batman", "Iron Man"]
movies.clear()
print(movies)

# index():- returns position of item
movies = ["Avengers", "Batman", "Iron Man"]
print(movies.index("Iron Man")) # 2

# count():- counts the items
movies = ["Avengers", "Batman", "Batman"]
count = movies.count("Batman")
print(count)

# sort():- sorts item alphabetically
movies = ["Joker", "Avengers", "Batman"]
movies.sort()
print(movies)

# reverse():- reverse the list
movies = ["Joker", "Avengers", "Batman"]
movies.reverse()
print(movies)

# copy():- creates a duplicate list
movies = ["Joker", "Avengers", "Batman"]
newMovies = movies.copy()
print(movies is newMovies) # False


# extend():- adds elements from another list
marvel_movies = ["Avengers", "Batman"]
dc_movies = ["Batman", "Joker"]

marvel_movies.extend(dc_movies)
print(marvel_movies)


# Loop through a list for loop
movies = ["Joker", "Avengers", "Batman"]

for movie in movies:
    print(movie)
    
# Loop through a list while loop
movies = ["Joker", "Avengers", "Batman"]
i = 0
while i < len(movies):
    print(movies[i])
    i += 1
    
# combine two lists using +
marvel_movies = ["Avengers", "Batman"]
dc_movies = ["Batman", "Joker"]
print(marvel_movies + dc_movies)