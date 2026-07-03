# Set:- Set is a collection of unique value.

players = {"Rohit", "Virat", "Gill", "Rahul"}
print(players, type(players), len(players))

# Duplicate values are not allowed in set
players = {"Rohit", "Virat", "Gill", "Rahul", "Rohit"}
print(players)

# Set is unordered (random order)
players = {"Rohit", "Virat", "Gill", "Rahul"}
print(players)

# Create set using set() method
team = set(["Rohit", "Virat", "Gill", "Rahul"])
print(team)

# Create empty set using set()
empty_set = set()
print(empty_set)

# Loop through set players
players = {"Rohit", "Virat", "Gill", "Rahul"}
for player in players:
    print(player)
    
# Add element to set
players = {"Rohit", "Virat", "Gill", "Rahul"}
players.add("Surya")
print(players)

# Add multiple elements to set
players = {"Rohit", "Virat", "Gill", "Rahul"}
players.update(["Hardik", "Jadeja"])
print(players)

# Remove item using remove() (error if item no found)
players.remove("Gill")
print(players)

# Remove item using discard() (no error if player is not found)
players.discard("Gill")

# pop() removes a random item
players.pop()
print(players.pop(), players) 

# clear() remove all players
temp_team = {"Rohit", "Virat"}
temp_team.clear()
print(temp_team)

# Membership check
players = {"Rohit", "Virat", "Gill", "Rahul"}
print("Rohit" in players)

# Union of two sets 
team_a = {"Rohit", "Virat", "Gill"}
team_b = {"Hardik", "Jadega", "Virat"}
print(team_a | team_b)
print(team_a.union(team_b)) # {'Virat', 'Hardik', 'Rohit', 'Gill', 'Jadega'}
print(team_a, team_b) 

# Intersection (Common items)
print(team_a & team_b)
print(team_a.intersection(team_b))

# Difference (returns items in team_a but not in team_b)
print(team_a - team_b)
print(team_a.difference(team_b))

# Symmetric Difference (returns items in either team_a or team_b but not both)
print(team_a ^ team_b)
print(team_a.symmetric_difference(team_b))

# copy() creates a new set
team_a = {"Rohit", "Virat", "Gill"}
team_b = team_a.copy()
print(team_b)

# subset check (check all values in the left set are present in the right set)
small_team = {"Rohit", "Virat"}
big_team = {"Rohit", "Virat", "Gill"}
print(small_team.issubset(big_team))

# superset check (check all values in the right set are present in the left set)
big_team = {"Rohit", "Virat", "Gill"}
small_team = {"Rohit", "Virat"}
print(big_team.issuperset(small_team))

# disjoint check (no common values)
team_a = {"Rohit", "Virat"}
team_b = {"Hardik", "Jadega"}
print(team_a.isdisjoint(team_b))