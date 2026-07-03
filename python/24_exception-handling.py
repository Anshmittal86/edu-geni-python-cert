# Exception :- An exception is an error that occurs during the execution of a program. It is a problem that interrupts the normal flow of the program and prevents it from executing the rest of the code.

print("Start")

try:
    print("I am working code")      # This code may raise an exception
except:
    print("An exception occurred")  # This code will run if an exception occurs
finally:
    print("I am always running...") # This code will always run

print("END")