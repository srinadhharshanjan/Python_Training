#Day 4: Lists and Tuples``
a = []
for i in range(1,5):
    list = input("Enter a value: ")
    a == list
    a.append(list)
print(a)

print(a[0])
a.append("rhyme")
print(a)
a.pop()
print(a)


fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
print(fruits)
print(fruits[5:0:-1])
fruits.append("grape")
#fruits.remove("banana")
fruits.pop(1)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits)
fruits.insert(2, "melon")
print(fruits)
print(len(fruits))

vegies = ("carrot", "potato", "onion", "cabbage")
print(vegies[-1])

my_tuple = (10, 20, 30, 20, 40, 50)

# Length
print(len(my_tuple))  # 6

# Count
print(my_tuple.count(20))  # 2

# Index
print(my_tuple.index(30))  # 2

# Minimum
print(min(my_tuple))  # 10

# Maximum
print(max(my_tuple))  # 50

# Sum
print(sum(my_tuple))  # 170



#Empty list
my_list = []
list_cout = int(input("Enter the number of items you want to add: "))
for i in range(list_cout):
    item = input("Enter an item: ")
    my_list.append(item)

    print("\nCurrent List:")
    for element in my_list:
        print(element)
