array = [1,1,2,2,2,3,4,4,5]
seen = []
for i in array:
    if i not in seen:
        seen.append(i)
print(seen)
