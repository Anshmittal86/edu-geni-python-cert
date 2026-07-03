# -------------------------------
# IF Statement
# -------------------------------

rating = 8.5
if rating > 8:
    print("This movie is superHit.")

# Note:- Statement is a code which can not be convert to a single value and expression is a code which can be convert to a single value.

# -------------------------------
# IF Else Statement
# -------------------------------

age = 15

if age >= 18:
    print("You can watch this movie.")
else:
    print("You cannot watch this movie.")
   
    
# -------------------------------
# IF Elif Else Statement
# -------------------------------

movie_rating = 7

if movie_rating >= 8:
    print("Blockbuster Movie")
elif movie_rating >= 6:
    print("Good Movie")
else:
    print("Average Movie")
    

# -------------------------------
# Nested IF ELSE
# -------------------------------

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
       print("Entry allowed Enjoy the movie!") 
    else:
       print("Buy a ticket first.")
else:
    print("You are not allowed to watch this movie")