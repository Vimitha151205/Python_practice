word = input()
temp = word.lower()
if temp == temp[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")