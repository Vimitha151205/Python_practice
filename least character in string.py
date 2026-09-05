s = input()
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1
        
min_freq = min(freq.values())
for ch in s:
    if freq[ch] == min_freq:
        print(ch)
        break 