while True:
    String1 = input("Enter a word1:")
    String2 = input("Enter a word2:")

    String1 = sorted(String1.lower())
    String2 = sorted(String2.lower())

    if String1 == String2:
        print("It is a Anagram")
    else:
        print("It is not a Anagram")

    
