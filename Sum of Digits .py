# Sum of Digits 
num = int(input('Enter a number:'))
sum = 0
while num > 0:
    valueStore = num % 10 
    sum = sum + valueStore
    num //= 10
print(sum)