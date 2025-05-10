# Largest of Three Numbers 
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
num3 = int(input('Enter thrid number:'))

if num1 == num2 == num3:
    print('All are same')
elif num1 >= num2 and num1 >= num3:
    print('Num1 is Greater')
elif num2 >= num1 and num2 >= num3:
    print('Num2 is Greater ')
else:
    print('Num3 is Greater')