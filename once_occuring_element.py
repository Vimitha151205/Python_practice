array = [1,1,2,2,2,3,4,4,5,5,5,5]
freq={}
for ch in array:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1
print("[" , end="")
for i in freq:
    print(f"[{i}:{freq[i]}]" , end="")
    
print("]")
        
