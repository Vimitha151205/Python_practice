arr = list(map(int, input().split()))
min_value = float('inf')
index = 0
for i in range (0,len(arr)):
    if arr[i] < min_value:
        min_value = arr[i]
        index = i
print(min_value)
print(index)
    
                  