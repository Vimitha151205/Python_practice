nums = list(map(int,input().split()))
count = []
repeated = []
for i in nums:
    if i in count:
        repeated.append(i)
    else:
        count.append(i)
repeated.sort()
print(repeated)
