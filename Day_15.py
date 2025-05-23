def my_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

greet("Ravi")
