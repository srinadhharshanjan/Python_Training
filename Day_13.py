class Car:
    def __init__(self):
        self.speed = 100         # Public
        self._gear = 3           # Protected (by convention)
        self.__engine_code = "XYZ123"  # Private

car = Car()
print(car.speed)         # ✅ Accessible
print(car._gear)         # ⚠️ Technically accessible, but discouraged
#print(car.__engine_code) #❌ Error: AttributeError
print(car._Car__engine_code)  # ✅ Works using mangled name


class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("❌ Insufficient funds")

    def show_balance(self):
        print(f"💰 Balance: ₹{self.__balance}")

b = Bank()
b.deposit(1000)
b.withdraw(300)
b.show_balance()  # ₹700
#print(b.__balance) #❌ Won’t work
print(b._Bank__balance) #✅ Works

class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = {}

    def add_mark(self, subject, mark):
        self.__marks[subject] = mark

    def get_marks(self):
        return self.__marks

s1 = Student("Anjali")
s1.add_mark("Math", 95)
print(s1.get_marks())
print(s1._Student__marks)

#Polymorphism
# Polymorphism allows methods to do different things based on the object it is acting upon.
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Polymorphism in action
for animal in [Dog(), Cat(), Animal()]:
    animal.sound()


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area = π × r²")

class Square(Shape):
    def area(self):
        print("Area = side × side")

shapes = [Circle(), Square()]
for shape in shapes:
    shape.area()

