#Lambda function
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

is_even = lambda x: x % 2 == 0
print(is_even(6))  # True

sub = lambda a,b,c:a-b-c
print(sub(10,2,3))

#Map function
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9, 16]

#Filter function
nums = [5, 10, 15, 20]
divisible_by_10 = list(filter(lambda x: x % 10 == 0, nums))
print(divisible_by_10)  # [10, 20]

#Reduce function
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
