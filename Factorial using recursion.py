# Factorial of a Number
# import math
# num = int(input('Enter a number:'))
# print(math.factorial(num))

# Factorial of a Number using recursion
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
print(fact(0))
