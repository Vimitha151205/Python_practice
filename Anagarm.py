while True:
    String1 = input("Enter a word1:")
    String2 = input("Enter a word2:")

    word1 = String1.lower()
    word2 = String2.lower()

    freq1={}
    freq2={}

    for ch in word1:
        if ch in freq1:
            freq1[ch] +=1
        else:
            freq1[ch] = 1

    for ch in word2:
        if ch in freq2:
            freq2[ch] +=1
        else:
            freq2[ch] = 1

    if freq1 == freq2:
        print("The word is a Anagram")
    else:
        print("The word is not a Anagram")

        
    

               
