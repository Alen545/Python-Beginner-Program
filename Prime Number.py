# Prime Number
num = int(input('Enter a Number:'))
counter = 0

for i in range(1,num + 1):
   
    if num % i == 0:
        counter += 1

if counter > 2:
    print('Not a prime')
else:
    print('Prime')