# Check Anagram
text1 = str(input('Enter a String:')).lower()
text2 = str(input('Enter a String:')).lower()

count = 0

for char in text1:
    if char in text2:
        count += 1

if count == len(text2):
    print('Anagram')
else:
    print('Not')
