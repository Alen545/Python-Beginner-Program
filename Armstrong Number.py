# Armstrong Number 
num = int(input('Enter a Number:'))
copynum = num
sum = 0
while num!=0:
    digit = num % 10
    sum = sum + pow(digit,3) 
    num = num // 10

if sum == copynum:
    print("Armstrong Number")
else:
    print("Not")



    
   