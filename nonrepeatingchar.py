string = input("Enter a word:")
freq={}
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
for i in freq:
    if freq[i] >= 2:
        print("Non-repeating character = " , end="")
        print(i)
        break
