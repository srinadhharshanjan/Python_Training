name = "Alice"
age = 30
print("Hello, %s! and age is %d" % (name, age))  # Old style formatting

name1 = "Bob"
print("Hello, {}!".format(name1))

name2 = "Charlie"
print(f"Hello, {name2}!")  # f-string

character = input("Name your character: ")
enemy = input("Name the enemy: ")
print(f"{character}: You won't get away with this, {enemy}!")
print(f"{enemy}: Try and stop me, {character}!")

# Squares
squares = [x**3 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
print(squares)

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
odds = [x for x in range(10) if x % 2 != 0]
print(odds)
print(evens)

for x in range(1, 6):
    if x % 2 == 0:
        print("x is even",x, end=" ")
    else:
        print("is odd",x, end=" ")

sentence = "The quick brown fox jumps over the lazy dog"
my_list = [len(word) for word in sentence.split()]
print(my_list)
