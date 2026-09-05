array = [1,1,2,2,2,3,4,4,5,5,5]
freq={}
for ch in array:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1
for i in freq:
    print("[",end ="")
    print(f"[{i}:{freq[i]}",end="")
print("]")
minimum = min(freq.values())
for i in freq:
    if freq[i] == minimum:
        print(f"minimum freqency number is = [{i} : {freq[i]}]" , end="")
     
