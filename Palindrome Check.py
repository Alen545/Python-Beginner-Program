#Check if a string is a palindrome
text = str(input('Enter a String:')).lower().replace(" ","")

if text == text[::-1]:
    print('String is Palindrome',text)
else:
    print('String is not palindrome')



