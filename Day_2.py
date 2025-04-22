age = 23
name = "John Doe"
print("my name and age is",name,age)
print(f"my name is {name} and my age is {age}")
print("my name is {} and my age is {}".format(name,age))


birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year
if age < 0:
    print("Invalid birth year.")
elif age > 0:
    print("You were age was ",age)
else: 
    print("You are born this year.")
# print(f"You are {age} years old.")

x=5
y=10
if x>y:
    print("x is greater than y")
else:
    print("x is less than y")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
elif a != b:
    print(f"{a} is not equal to {b}")
elif a >= b:
    print(f"{a} is greater than or equal to {b}")
elif a <= b:
    print(f"{a} is less than or equal to {b}")
else:
    print("Invalid input")

if a<=b and c>=d:
    print("AND worked")
elif a<=b or c<=d:
    print("OR worked")
elif a!= b:
    print("NOT worked")
else:
    print("Invalid input")

