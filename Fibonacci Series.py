# first N Fibonacci numbers using recursion
num_value = int(input('Enter the number:'))

firstDigit,secondDigit = 0,1
count = 0

while count < num_value:
    print(firstDigit,end='')
    firstDigit,secondDigit = secondDigit, firstDigit+secondDigit
    count += 1
    