string = input("Enter a word:")
freq={}
for ch in string:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1
minimum = min(freq.values())
for i in freq:
    if freq[i] == minimum :
        print(i)
        
        
