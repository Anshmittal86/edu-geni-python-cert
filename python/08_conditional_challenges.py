# Challenge 1: Super Hit Detector
# Take movie rating as input from the user.
# If the rating is 8 or higher, print Super Hit Movie.

movie_rating = float(input("Enter movie rating: "))

if movie_rating >= 8:
    print('Super Hit Movie.')

# Challenge 2: Age Gatekeeper
# Take age as input from the user.
# If the age is 18 or above, print Allowed for Adult Movie.
# Otherwise, print Not Allowed.

age = int(input("Enter your age: "))

if age >= 18:
    print('Allowed for Adult Movie')
else:
    print('Not Allowed')

# Challenge 3: Movie Quality Classifier
# Take movie rating as input from the user.
# If the rating is 8 or higher, print Blockbuster.
# If the rating is between 6 and 7.9, print Good Movie.
# Otherwise, print Average Movie.

movie_rating = float(input("Enter movie rating: "))

if movie_rating >= 8:
    print('Blockbuster')
elif movie_rating >= 6:
    print('Good Movie')
else:
    print('Average Movie')
    
    
# Challenge 4: Ticket Price Checker
# Take ticket price as input from the user.
# If the price is greater than 300, print Expensive Ticket.
# Otherwise, print Affordable Ticket.

ticket_price = float(input("Enter ticket price: "))

if ticket_price > 300:
    print('Expensive Ticket')
else:
    print('Affordable Ticket')

# Challenge 5: Duration Analyzer
# Take movie duration in minutes as input from the user.
# If the duration is greater than 180, print Long Movie.
# If the duration is greater than 120, print Normal Movie.
# Otherwise, print Short Movie.

movie_duration = float(input("Enter movie duration: "))

if movie_duration > 180:
    print('Long Movie')
elif movie_duration > 120:
    print('Normal Movie')
else:
    print('Short Movie')

# Challenge 6: Entry Permission System
# Take age and has_ticket as input from the user.
# If age is greater than or equal to 18 and has_ticket is True, print Entry Allowed.
# Otherwise, print Entry Denied.

# Hint: You will need to convert the ticket input from string to boolean. 

# Challenge 7: Genre Identifier
# Take movie genre as input from the user.
# If the genre is Action, print High Energy Movie.
# If Comedy, print Fun Movie.
# If Horror, print Scary Movie.
# Otherwise, print Different Genre.

# Challenge 8: Rating Master Judge
# Take movie rating as input from the user.
# If the rating is 9 or higher, print All Time Classic.
# If the rating is between 7 and 8.9, print Must Watch.
# If the rating is between 5 and 6.9, print One Time Watch.
# Otherwise, print Skip It.

# Challenge 9: Kids vs Adults Review System
# Take age and movie_rating as input from the user.

# Rules:
# If age is less than 18:
#  If rating is greater than 8, print Kid Friendly Hit.
#  Otherwise, print Kid Friendly Average.

# If age is 18 or above:
#  If rating is greater than 8, print Adult Super Hit.
#  Otherwise, print Adult Average.

# Challenge 10: Ultimate Cinema Entry Logic
# Take three inputs from the user:
# age
# has_ticket
# is_vip

# Rules:
# If age is less than 18, print Entry Denied.
# If age is 18 or above:
#  If has_ticket is True, print Entry Allowed.
#  Else if is_vip is True, print VIP Entry Allowed.
#  Otherwise, print Entry Denied.

age = int(input("Enter your age: "))
has_ticket = input("Do you have ticket(yes/no and Y/N): ")
is_vip = input("Do you have VIP ticket(yes/no and Y/N): ")

has_ticket = has_ticket == 'yes' or has_ticket == 'Y'
is_vip = is_vip == 'yes' or is_vip == 'Y'

if age < 18:
    print("Entry Denied")
elif has_ticket:
    print("Entry Allowed")
elif is_vip:
    print("VIP Entry Allowed")
else:
    print("Entry Denied")