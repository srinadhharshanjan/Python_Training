# my_dict ={"key1":"value1", "key2":"value2", "key3":"value3"}
# #print(my_dict)
# print(my_dict["key3"])

# # Dictionary of a student
# student = {
#     "name": "Alice",
#     "age": 21,
#     "course": "Python",
#     "email": "asd@asd.com"
# }

# # 1. get() - safe key access
# print(student.get("name"))         # Output: Alice
# print(student.get("email", "N/A")) # Output: N/A (default)

# # # 2. keys() - get all keys
# print(student.keys())              # Output: dict_keys(['name', 'age', 'course'])

# # # 3. values() - get all values
# print(student.values())            # Output: dict_values(['Alice', 21, 'Python'])

# # # 4. items() - key-value pairs
# print(student.items())             # Output: dict_items([('name', 'Alice'), ('age', 21), ('course', 'Python')])

# # # 5. update() - update or add new key-value
# student.update({"age": 22})
# student.update({"email": "alice@mail.com"})
# print(student)                     # Output: {'name': 'Alice', 'age': 22, 'course': 'Python', 'email': 'alice@mail.com'}

# # # 6. pop() - remove by key
# student.pop("course")
# print(student)                     # Output: {'name': 'Alice', 'age': 22, 'email': 'alice@mail.com'}


# student ["course"] = "java"
# print(student)   

# student ["class"] = "  programming  "                                           
# print(student)                     # Output: {'name': 'Alice', 'age': 22, 'course': 'java', 'email': '

# # print(student)                     # Output: {'name': 'Alice', 'age': 22, 'email': '
# # # 7. clear() - remove everything
# student.clear()
# print(student)                   # Output: {}

# # 8. in - check if key exists
# print("email" in student)          # Output: True
# print("course" in student)         # Output: False

# # 9. len() - number of key-value pairs
# print(len(student))                # Output: 3



# Sample sets
fruits = {"apple", "banana", "cherry"}
more_fruits = {"banana", "dragonfruit", "kiwi"}

# 1. add() - add item
fruits.add("mango")
fruits.add("mango")               # No error, but no duplicate added
print(fruits)                      # Output includes 'mango'

# # 2. remove() - remove item (error if not found)
# # fruits.remove("pineapple")      # ❌ Will raise KeyError
fruits.remove("banana")
print(fruits)                      # 'banana' removed

# # 3. discard() - remove item (no error if not found)
# fruits.discard("kiwi")             # No error even if kiwi not present
# print(fruits)

# # 4. union() - combine both sets
# all_fruits = fruits.union(more_fruits)
# print(all_fruits)                  # Combined unique items

# # 5. intersection() - common items
# common = fruits.intersection(more_fruits)
# print(common)                      # Output: {'dragonfruit'} or set of shared fruits

# # 6. difference() - items in fruits but not in more_fruits
# unique_to_fruits = fruits.difference(more_fruits)
# print(unique_to_fruits)

# # 7. clear() - remove all items
# # fruits.clear()
# # print(fruits)                   # Output: set()
