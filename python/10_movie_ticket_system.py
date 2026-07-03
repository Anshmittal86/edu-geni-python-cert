# Movie ticket booking system

print("Welcome to the Movie Theater")

movies = ["Avengers", "Batman", "Interstellar"]
ticket_price = 200

while True:
    print("\nAvailable Movies\n")
    
    for index in range(len(movies)):
        print(f'{index + 1} - {movies[index]}')
    
    choice = int(input("Select movie number (0 to exit): "))
    
    if choice == 0:
        print("Thank you for Visiting!")
        break
    
    if choice < 1 or choice > len(movies):
        print("Invalid choice. Try again.")
        continue
    
    tickets = int(input("How many tickets do you want ?: "))
    
    total_cost = tickets * ticket_price
    
    print(f"You selected: {movies[choice - 1]}")
    print(f"Total cost: {total_cost}")
    
    