nums = list(map(int, input().split()))
k=int(input())
count = 0
if k == 0:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for value in freq.values:
        if value > 1:
            count +=  1
else:
    s = set(nums)
    for num in s:
        if num + k in s:
            count += 1
print(count)
        

