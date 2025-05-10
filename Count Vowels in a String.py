# Count Vowels in a String 
text = str(input('Enter a String:'))

vowels = "a,e,i,o,u,A,E,I,O,U"

counter = 0

for char in text:
    if char in vowels:
        counter += 1
print(counter)