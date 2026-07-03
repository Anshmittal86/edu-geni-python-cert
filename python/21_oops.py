# 1. Basic Class and Object:- create a car class with attributes like brand and model. Then create an instance of this class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
my_car = Car("Lamborghini", "Aventador", "Ultra")
print(my_car.brand)
print(my_car.model)


# 2. Class Method and Self: Add a method to the Car Class that displays the full name of the car (brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        print(f"{self.brand} {self.model}")

my_car = Car("Toyota", "Camry")

print(my_car.brand)
print(my_car.model)

print(my_car.full_name())

# 3. Inheritance:- Create a ElectricCar class that inherit from the car class and has addtional attribute battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        print(f"{self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model 5", "100kwh")
print(my_tesla.battery_size)
print(my_tesla.brand)
print(my_tesla.model)

# 4. Encapsulation:- Modify the Car calss to encapsulate the brand attribute. making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        print(f"{self.brand} {self.model}")
        
my_car = Car("Toyota", "Camry")
print(my_car.get_brand())
print(my_car.__brand) # Error

# 5:- Polymorphism:- Demonstrate Polymorphism by defining a method fuel_type in both Car and ElectricCar with different behaviour

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def full_name(self):
        print(f"{self.brand} {self.model}")
        
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model 5", "100kwh")
print(my_tesla.fuel_type())

# 6:- Class Variables:- Add a class variable to Car that keeps track of the number of car created.

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def full_name(self):
        print(f"{self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model 5", "100kwh")
print(Car.total_car)


# 7. Static method:- Add a static method to the Car class that returns a general description of a car

# What is static method:- A static method is a method that is belongs to the class rathen than instance of the class. It is a class method and can be called without creating an instance of the class.

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def full_name(self):
        print(f"{self.brand} {self.model}")
    
    @staticmethod
    def general_description():
        return "Cars are means of transportation."


print(Car.general_description())


# 8. Property Decorator:- Use a property decorator to the Car class to make the model attribute read-only

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def full_name(self):
        print(f"{self.brand} {self.model}")
    
    @staticmethod
    def general_description():
        return "Cars are means of transportation."
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model 5", "100kwh")
print(my_tesla.model)

# 9. Class Inheritance and isinstance() Function:- 

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def full_name(self):
        print(f"{self.brand} {self.model}")
    
    @staticmethod
    def general_description():
        return "Cars are means of transportation."
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model 5", "100kwh")

print(isinstance(my_tesla, Car)) # True
print(isinstance(my_tesla, ElectricCar)) # True

# 10. Multiple Inhertiance:- Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance

class Battery:
    def battery_info(self):
        return "Battery Info"

class Engine:
    def engine_info(self):
        return "Engine Info"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model 5")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
print(my_new_tesla.full_name())