# def print_matrix():
#     rows = int(input("Enter the number of rows: "))
#     columns = int(input("Enter the number of columns: "))

#     matrix = []  # Empty matrix to store rows

#     for i in range(rows):
#         row = []
#         for j in range(columns):
#             value = input(f"Enter value for ({i},{j}): ")
#             row.append(value)
#         matrix.append(row)

#     print("\nPrinted 2D Matrix:")
#     for row in matrix:
#         for element in row:
#             print(element, end=" ")
#         print()  # New line after each row 

# # Call the function
# print_matrix()

# def mex():
#     for k in range(1, 3):
#         for l in range(1, 3):
#             print(k, l)
#         print()
# mex()


# def multi():
#     for i in range(1,11):
#         for j in range(1,21):
#             print(f"{i *j:4}", end=" ")
#         print()
# multi()

# try:
#     age = int(input("Enter your age: "))
#     if age <= 100:
#         print(f"You are {age} years old. ✅ Age is valid.")
#     else:
#         print(f"You are {age} years old. ⚠️ Age seems unrealistic.")
# except ValueError:
#     print("❌ Please enter a valid number.")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        print("Result:", num1 / num2)
    else:
        print("❌ Invalid operator!")

except ValueError:
    print("❌ Invalid number input.")
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")

