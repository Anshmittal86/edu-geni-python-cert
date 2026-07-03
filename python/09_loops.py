# Loops:- Loops is a block of code which is executed multiple times.

# for loop:- for loop is used to iterate over a sequence.
movies = ["Avengers", "Batman", "Interstellar"]
for movie in movies:
    print(movie)
    
    
# while loop:- while loop is used to iterate over a sequence based on the condition.
ticket = 3
while ticket > 0:
    print(f"Ticket: {ticket}")
    ticket -= 1
print('House full')

    
# range() with for loop
for number in range(1, 6):
    print(f"Number : {number}")
    
    
# break:- break used to exit the loop between
movies = ["Avengers", "Joker", "Batman"]

for movie in movies:
    if movie == "Joker":
        print(f"Movie Found! {movie}")
        break

# continue:- continue used to skip the current iteration of the loop
movies = ["Avengers", "Slow movie", "Batman"]

for movie in movies:
    if movie == "Slow movie":
        continue
    print(f"Recommended: {movie}")