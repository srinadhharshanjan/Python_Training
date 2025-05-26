# Python_Training
Day-2 Notes
Print 
Input
print statement types

Custom words, Key words 

DataTypes
Variable?


Variable  ---> The one which can change or mutable one 
COnstant  ----> which cannot change Immutable

5

a  =  ?? 
c  = ??

Int ---> Integer
Float -- > Floating Value
Boolean  
String 


Integer --> whole Numbers (from 0 to infinite)  ----> int
Float ---> Numbers with deciamals		----> float
String ---> Text or characters			----> str
Boolean ---> True or False			----> bool


Print Statement ---> used to print a statement
syntax == print("write whatever you want in quotes only")

Input Statement
a = input("write a number")

def devi(a,b)
def
print
int
if
else
for
while
true
false


Day-3 Notes

if 
elif
else


if condition 

x =2 
if x=2 
then print as x is true 

elif x =3
 then print as x is false

else
value is wrong 


Operators
Arthemetic Operators  --->    +, -, *, ....

Comparision Operations  -----> <,>, ==, <=, >= ,!=

Logical Operators  ------>  AND, OR, NOT

AND

X     Y    X AND Y  &&
T     T      T
T     F      F
F     T      F
F     F      F


OR
X    Y    X OR Y  ||
T    T      T
T    F      T
F    T      T
F    F      F

NOT
X      ~X   !=
T	F
F	T


Comparision operators

a<b 2<3
a>b  3>2
a<=b  a can be less or eaqual to b but not greater than b
a>=b  a can be greater or equal to b but not less than b
a!=b  a can be anything but not b
a == b both are same
day _ 4 notes

Day_ 4 concepts --- > Loops

why we use loops means to repeat the tasks 

for 
while 


range --> function 

range (1,10, 2)

1 ---> start of range

10 ----> end of range

2 ----> step function 


range ( 10)

starting wil be 0 always 

step will be 1 as default 

for i in range(1,10)
	print (i)

loop controllers
 break ---> to stop the loop
 continue ---> to skip that current iteration and continue


While loop ---> conditioned based loop 

while condition :
 print


Day_5 ---> Lists and Tuples

List -- []
tuple --- ()

Lists are always mutable 
tuples are immutable 


anything which you want to store that can be changed in the future should be a list 

anything which you dint want to change in the future should be in a tuple

List Functions
append ---> to add an item at the end of the list
sort  ----> to sort the list
pop   ----> to remove an element form the list based on the index
remove ----> remove the last element

Tuple Functions
min 
max
count
len

Day_6---> Dictionaries & Sets

int
float
char
Boolean
tuple
list
string
Dict 
set 

Dictionary : {"key" :"value1", ...........}
set :{"key1","key2",.............}


Day 7 ---> Functions

predefied or user defined code blocks that are reusable and used by user in various aspects of his coding.

it starts "def" keyword 

Syntax:

def any_name_of_the_function(paramerters as required):
	code block


	return value

Day - 9 ----> String Functions 

Split() ----> any particular key value based divide the string 
strip()-----> to remove empty spaces 
replace() -----> to replace one word with another 
join() -----> to combine words after splitting 

Day - 10  ----> String formatting


print("")

print(f" {}")

print("hello .format.{}")

name = time
print("%s" %name)


Day -11 ---> list comprehensions

[expression for item in iterable if condition]

my_list = [x**2 for x in range(5)]


Day-14

Function	Purpose
 open()	        Opens a file
.read()	        Reads the whole file
.readline()	Reads one line at a time
.write()	Writes to a file
 with	        Used as a context manager
'r' / 'w' / 'a'	File modes: read / write

Day-15

CSV (Comma Separated Values)
Used for spreadsheets or tables

JSON (JavaScript Object Notation)
Used for structured data like dictionaries/lists


Module	Function
csv	csv.reader, csv.writer
json	json.load, json.dump

Day 16 & 17


CRUD ---> Create, Read, Update, Delete

What is Object-Oriented Programming (OOP)?
OOP is a programming paradigm where you structure code using objects and classes. It helps:

Reduce repetition

Improve modularity

Enhance reusability and scalability

What is a Class?
A class is like a blueprint for creating objects. It defines:

Attributes (variables/data)

Methods (functions/actions)
class Dog:
    # This is a class
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

What is an Object?
An object is a specific instance of a class.
You create it using the class:
my_dog = Dog("Bruno", "Labrador")

The __init__() Method
A special method (constructor) that initializes object attributes when the object is created.

self refers to the current object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


The self Keyword
Always the first parameter of instance methods.

Refers to the current object.

Used to access attributes and methods.

Instance Attributes
Defined in __init__()

Specific to each object

🔹 Instance Methods
Functions defined inside the class

Use self to access attributes or call other methods

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius



Key Concepts Comparison

Concept			Description
class			Blueprint for objects
object			An instance of a class
__init__()		Constructor method
self			Reference to the current object
Instance Attribute	Variable tied to each object
Method			Function defined inside a class


What is a Constructor in Python?
A constructor is a special method that is automatically called when an object is created from a class. It is used to initialize the object’s properties (attributes).

 In Python, the constructor is the __init__() method.

Opposite of Constructor: Destructor
A destructor is a method that is called automatically when an object is deleted or destroyed, usually to clean up resources like files or network connections.

In Python, the destructor is the __del__() method.


Day-18

What is Inheritance?
Inheritance allows one class (child/subclass) to inherit the properties and methods of another class (parent/base class).

✅ Why Use Inheritance?
Reuse code

Maintain consistency across related classes

Add or extend features in child classes

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

obj = Child()
obj.greet()         # Inherited from Parent
obj.greet_child()   # From Child


What is super() in Python?
The super() function is used to call a method from a parent (or superclass) inside a child class.


Why use super()?
When a child class overrides a method from its parent class (like _init_() or attack()), you might still want to reuse part of the parent's method. Instead of rewriting the same code again, super() helps you reuse the parent’s functionality.


Day-19

Encapsulation & Private Variables

Encapsulation = Hiding internal data and showing only what is necessary through methods.

What is Encapsulation?
Encapsulation is the OOP principle of binding data (variables) and methods (functions) that operate on that data into a single unit, called a class.
It also involves restricting direct access to some components of an object to protect the integrity of the data.

Why Encapsulation?
✅ Prevents unauthorized access to sensitive data

✅ Makes code modular and easier to debug

✅ Allows validation and control using getter/setter methods

✅ Hides complexity from the user

Python Access Modifiers
Type	Syntax	Accessibility
Public	self.value	Accessible everywhere
Protected	self._value	Shouldn't be accessed outside the class
Private	self.__value	Name mangled, access limited to class only

Python doesn’t have real "private" — it uses name mangling.

Access Modifiers in Python:

public: accessible everywhere (default)

_protected: conventionally internal use only

__private: name mangled, meant to be truly private


Real-Life Analogies
Real Life	Python Encapsulation
ATM card	Class
Card PIN	Private variable
Withdraw screen	Public method (withdraw)
Bank software	Encapsulated logic

Day_20

What is Polymorphism?
Polymorphism means "many forms".
In programming, it allows objects of different classes to be treated as objects of a common superclass, while still calling their specific implementations.

🔁 In Python, this often happens through method overriding and duck typing (if it walks like a duck...).


Key Concepts
Concept	Description
Polymorphism	Different classes implement the same method differently
Method Overriding	Subclass redefines a method from the parent class
Duck Typing	Python relies on method names and behavior rather than strict types

Real-World Analogy
Situation	Polymorphism Example
Payment systems	.pay() might work differently in UPI, credit card, or PayPal classes
UI Components	.draw() can differ for buttons, sliders, checkboxes
File Readers	.read() method works for CSV, JSON, or TXT readers

Day_21

Lambda Functions (Anonymous Functions)
✅ What are they?
A lambda function is a small, anonymous function created using the lambda keyword. It can have any number of arguments, but only one expression.

Syntax:
lambda arguments: expression

Where it's used:
When a short function is needed temporarily, like in map(), filter(), or sorting.

Used in GUI buttons, data transformation, or sorting custom objects.

map(function, iterable)
✅ What is map()?
Applies a function to every item in an iterable (like a list, tuple).

Returns a map object (which can be converted to list, tuple, etc.)

map(function, iterable)

Real-World Use:
Converting all user inputs from string to int

Applying discounts to a list of prices

Converting temperature values

filter(function, iterable)
✅ What is filter()?
Returns only those items from an iterable for which the function returns True

Good for extracting a subset of data

filter(function, iterable)
Real-World Use:
Filtering valid email addresses

Keeping students who passed

Removing empty or zero values

4. reduce(function, iterable)
✅ What is reduce()?
Applies a function cumulatively to the items of an iterable.

Unlike map() and filter(), it reduces the iterable to a single value.

To use reduce(), you must import it from functools.

from functools import reduce
reduce(function, iterable)

Real-World Use:
Summing values

Finding factorial

Combining strings

Aggregating scores, profits, etc.

Comparison Table
Feature			lambda			map()		filter()				reduce()
Use Case	Create quick function	Transform values	Filter values based on condition	Reduce to single value
Returns			Function	map object (iterator)	filter object (iterator)		Single value
Import?			No			No		No					Yes (functools)
Can use lambda?		✅ Yes			✅ Yes		✅ Yes					✅ Yes

Real-World Applications
Use Case				Tool Used
Clean up user data			map(), lambda, strip()
Filter valid email addresses		filter()
Aggregate total sales from data		reduce()
Remove empty responses from survey	filter()
Increase salary by 10%			map()
Calculate average, sum, or product	reduce()

Day - 22
Theory: What is a Decorator?
A decorator is a function that takes another function as input, adds extra functionality, and returns the new function — without modifying the original function's code.

Think of decorators as wrapping functions — like giving your game character an extra power-up without changing who they are.

How It Works
@my_decorator applies the wrapper function around say_hello.

This is function wrapping.


What is a Decorator?
A decorator is a higher-order function — it takes another function as an argument, adds some functionality to it, and returns a new function. It's a form of metaprogramming, meaning your code modifies other parts of your code.

Why Use Decorators?
They allow code reuse, separation of concerns, and dynamic behavior extension of functions or methods without modifying their source code.


Common use cases include:

Logging

Caching

Access control / authentication

Input validation

Performance monitoring

Pre/post conditions for testing

In Code Terms:
A decorator is a function that:

Takes another function as input,

Adds some new behavior to it (before or after),

Then returns the updated function.




def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code before function
        result = original_function(*args, **kwargs)
        # Code after function
        return result
    return wrapper_function

What is **kwargs in Python?
**kwargs stands for "keyword arguments". It allows a function to accept any number of named arguments (i.e., arguments passed with a name, like age=25), and it collects them into a dictionary.

Real-World Use Cases

Use Case			Example
Logging				@log_action 	logs calls to a function
Access Control			@login_required in Django
Timing				@timer 		decorator to measure execution time
Testing				@pytest.mark.skip, @unittest.skip
Web Frameworks			Flask uses @app.route('/home') to define endpoints
Game Mechanics			@boost, @shield for dynamic player state changes

Day-23


What is a Module?
A module is a Python file (.py) that contains definitions and statements — typically functions, classes, or variables.

What is a Package?
A package is a collection of modules in a directory with a special __init__.py file.

shop/
│
├── __init__.py
├── inventory.py
└── billing.py

# inventory.py
def show_items():
    return ["Sword", "Potion", "Shield"]
# billing.py
def total_price(items):
    prices = {"Sword": 100, "Potion": 50, "Shield": 150}
    return sum(prices[item] for item in items)
# main.py
from inventory import show_items
from billing import total_price

items = show_items()
print("Items:", items)
print("Total:", total_price(items))


Day-24
Virtual Environment (venv)
A virtual environment is an isolated Python environment to manage dependencies for a project.

python -m venv myenv


Pip - Python Package Installer
Use pip to install external libraries.