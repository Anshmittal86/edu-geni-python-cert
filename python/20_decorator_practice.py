import functools
import time

# Task 1: Function Execution Logger

def print_function_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running Function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending Function: {func.__name__}")
        return result
    return wrapper

@print_function_name
def sayHello():
    time.sleep(2)
    print("hello")
    
sayHello()