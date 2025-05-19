class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

obj = Child()
obj.greet()         # Inherited from Parent
obj.greet_child()   # From Child


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

d = Dog("Buddy")
c = Cat("Whiskers") 
d.speak()  # Output: Buddy says Woof!
c.speak()  # Output: Whiskers says Meow!

class Creature:
    def __init__(self, name):
        self.name = name

    def attacks(self):
        print(f"{self.name} attacks!")

    def blame(self):
        print(f"{self.name} blames someone else!")

class Dragon(Creature):
    def attack(self):
        super().attacks()
        super().blame()
        print(f"{self.name} breathes fire!")

class Goblin(Creature):
    def attack(self):
        super().attacks()
        super().blame()
        print(f"{self.name} swings a club!")

d = Dragon("Smaug")
g = Goblin("Grub")
e = Creature("Generic Creature")
# d.attack()  # Output: Smaug breathes fire!
g.attack()  # Output: Grub swings a club!   
# e.attack()  # Output: Generic Creature attacks!
d.attack()  # Output: Smaug breathes fire!

class Vehicle:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

class Car(Vehicle):
    def speed_info(self):
        print(f"Speed: {self.speed}")

    def capacity_info(self):
        print(f"Capacity: {self.capacity}")

class Bus(Vehicle):
    def speed_info(self):
        print(f"Speed: {self.speed}")

    def capacity_info(self):
        print(f"Capacity: {self.capacity}")

# Create objects
a = Car("40 km", "4 members")
b = Bus("50 km", "20 members")

# Call methods
a.speed_info()
a.capacity_info()
b.speed_info()
b.capacity_info()
