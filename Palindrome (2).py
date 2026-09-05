while True:
    String = input("Enter a word:")
    str = String.lower()
    if str == "exit":
        break
    if str == str[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
    
