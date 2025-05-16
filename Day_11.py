class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

car1 = Car("Toyota", 120)
car2 = Car("Honda", 100)
print(car1.brand)  # Output: Toyota
print(car1.speed)  # Output: 120
print(car2.brand)  # Output: Honda
print(car2.speed)  # Output: 100
print(car1.brand, car2.brand)



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
c1 = Circle(5)
print(c1.area())   # Area of circle
c1.radius = 10
print(c1.area())   # Updated area


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"{self.name}'s balance: ₹{self.balance}")

# 🔸 Creating an object of BankAccount
account1 = BankAccount("Amit", 1000)

# 🔸 Performing some operations
account1.deposit(500)         # Deposit ₹500
account1.withdraw(300)        # Withdraw ₹300
account1.display()            # Display current balance



class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0

    def gain_xp(self, points):
        self.xp += points
        print(f"{self.name} gained {points} XP.")

    def check_level_up(self):
        if self.xp >= 100:
            self.level += 1
            self.xp -= 100
            print(f"{self.name} has leveled up to {self.level}!")
        else:
            print(f"{self.name} needs more XP to level up.")

# 🔹 Creating a hero
hero1 = Hero("Arjun")

# 🔹 Gaining XP and checking level up
hero1.gain_xp(50)
hero1.check_level_up()

hero1.gain_xp(60)
hero1.check_level_up()

# 🔹 Display final stats
print(f"\nFinal Stats → Name: {hero1.name}, Level: {hero1.level}, XP: {hero1.xp}")


class Student:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created.")

    def __del__(self):
        print(f"{self.name} has been destroyed.")
s1 = Student("Ravi")
s2 = Student("Raj")
l1 = Student("gamer")
del s1  # Manually deleting the object
