for i in range(1,10):
    if i == 8:
        break
    print(i)

for seconds in range(5,0,-1):
    print(f"timer in {seconds} seconds")
    secret_code = input("Enter a code: ")
    if secret_code == "1234":
        print("Bomb defused !!!!")
        break
else:
    print("Boom! Game over.")

count = int(input("Enter a number: "))
while count <= 5:
    print("Hello World")
    count += 1
    break   
else:
    print("error count is greater than 5")

secret = 7
guess = int(input("Guess the number (1-10): "))

while guess != secret and guess < 3 or guess < 9:
    print("Wrong guess. Try again.")
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("You guessed it!")
        break
else:
    print("You failed to guess the number.")

#The below code is an example of an infinite loop that will run until the user enters 0 a primary number 
sum = 10
value = int(input("Enter a number: "))
while value !=0:
    print("the value will be printed till it reaches the sum")
    value += 1
    if value < sum:
        print("sum is greater than the number")
    elif value > sum:
        print("sum is less than the number")
    if value == sum:
        print("sum is equal to the number")
        break
else:
    print("sum is greater than the value")

#The below code is an alternative way to implement the same logic and stop the infinite loop.
sum = 10
value = int(input("Enter a number: "))

while value != 0:
    if value < sum:
        print("sum is greater than the number")
    elif value > sum:
        print("sum is less than the number")
    else:  # value == sum
        print("sum is equal to the number")
        break
    
    # Ask again to avoid infinite loop
    value = int(input("Enter a number: "))
else:
    print("sum is greater than the value")


print("go on")
for step in range(1, 10):
    print("step", step)
    if step == 5:
        print("stop")
        break

# pattenrn printing alternativiely 
for i in range(1,10):
    print (i)
    if i == 5:
        print ("*")
        continue
    print ("#")


for i in range(10,0,-1):
    print(i)



value = int(input("Enter a number: "))
while value != 0:
    print ("*")
    value  += 1
    break
else: 
    print("value should not be zero")


rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
letter = 65
alphabet = 'A'
for i in range(rows):
    for j in range(cols):
        print(chr(letter), end=" ")
        letter += 1
    print()

for r in range(rows):
    for c in range(cols):
        print(alphabet, end=" ")
        alphabet = chr(ord(alphabet) +1)
    print()

for i in range(rows):
    print(chr(letter), end=" ")
    letter += 1

for j  in range(cols):
    print("*", end = " ")

for k in range (rows):
    print("*")