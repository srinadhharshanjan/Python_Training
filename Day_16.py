def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet():
    print("Hello!")
greet()

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
my_function(name="Alice", age=30, city="New York")

def demo(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

demo(1, 2, 3, name="Ravi", age=22)

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def greet(name):
    print(f"Hello, {name}!")

greet("Ravi")


def safe_division(func):
    def wrapper(a, b):
        if b == 0:
            return "❌ Cannot divide by zero."
        return func(a, b)
    return wrapper

@safe_division
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))
