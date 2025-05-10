inputValue = int(input('Enter a number:'))

for i in range(1,inputValue+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
