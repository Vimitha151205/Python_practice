n = int(input())
roll = list(map(int, input().split()))
seen = set()
deleted = 0
for i in roll:
    if i in seen:
        deleted +=1
    else:
        seen.add(i)
print(deleted)