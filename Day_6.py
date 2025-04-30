def welcome_user():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    return name
welcome_user()



def lister():
    my_list = []
    limit = int(input("Enter the maximum number of items to add: "))
    
    list_add = input("Enter the items separated by commas: ")
    list_add = list_add.split(",")

    for item in list_add:
        if len(my_list) < limit:
            my_list.append(item.strip())
        else:
            print("Limit reached! Extra items ignored.")
            break

    print("Final List:", my_list)

print(lister())


def trail1(a,b):
    if a == b:
        return True
    elif a != b:
        return False
    else:
        return False
    
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
opt = input("Enter an operator: ,==, != ")
if opt == "==":
    print(trail1(a,b))
elif opt == "!=":
    print(trail1(a,b))
else: 
    print("Invalid Operator")


def dicter():
    my_dict = {}
    limit = int(input("Enter the maximum number of items to add: "))
    
    for i in range(limit):
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        my_dict[key] = value

    print("Final Dictionary:", my_dict)
dicter()

def lister_1():
    my_List_1 = []

    limit = int(input("Enter the maximum number of items to add: "))

    for i in range(limit):
        item = input("Enter an item: ")
        my_List_1.append(item)  
        print(f"Added: {item}")

    print("\nFinal my_List_1:")
    for item in my_List_1:
        print(item)

    return my_List_1

# Call the function
lister_1()
