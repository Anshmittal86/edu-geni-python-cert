# Dictionary:- Dictionary is a collection of key-value pairs.

menu = {
    "Burger": 120,
    "Pizza": 250,
    "French Fries": 90
}
print(menu)

# Keys are unique but values can repeat
menu = {
    "Burger": 120,
    "Veg Burger": 120,
}
print(menu)

# Keys must be immutable (like string, number, tuple)
menu = {
    [1, 2, 3]: 120,
}
print(menu)

# Dictionary is ordered (Python 3.7+ keeps insertion order)
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 90
}
print(menu)

# Create dictionary using dict() function
menu = dict(Burger=120, Pizza=250, Fries=90)
print(menu)

# Create empty dictionary
empty_menu = {}
print(empty_menu, type(empty_menu))

# Access value using key 
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 90
}
print(menu["Burger"])

# Access value using get() method
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 90
}
print(menu.get("Burger", "Item not found"))

# Add new item to menu 
menu["Cold Drink"] = 60
print(menu)

# Updating existing item
menu["Burger"] = 150
print(menu)

# Remove item using pop()
menu.pop("Pizza")
print(menu)

# Remove item using del
del menu["Fries"]
print(menu)

# popitem() removes last inserted item
menu.popitem()
print(menu)

# clear() removes all items
menu.clear()
print(menu)

# Loop through dictionary
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 90
}

for item in menu:
    print(item) # Burger, Pizza, Fries
    
for value in menu.values():
    print(value) # 120, 250, 90
     
for key, value in menu.items():
    print(key, value) # Burger 120, Pizza 250, Fries 90
    
# Nested Dictionary
restaurant = {
    "Cafe1": {
        "Burger": 120,
        "Pizza": 250,
        "Fries": 90
    },
    "Cafe2": {
        "Burger": 110,
        "Pizza": 230,
        "Fries": 80
    }
}

print(restaurant["Cafe1"]["Burger"]) # 120

# Get all menu items (keys)
print(menu.keys()) # dict_keys(['Burger', 'Pizza', 'Fries'])

# Get all menu items (values)
print(menu.values()) # dict_values([120, 250, 90])

# Get all menu items (items)
print(menu.items()) # dict_items([('Burger', 120), ('Pizza', 250), ('Fries', 90)])

# update() adds or merge another dictionary
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 90
}

menu.update({"Sandwich": 150})
print(menu)

