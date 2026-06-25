n=int(input())
words = input().split()
max_len = 0
result = ""

for i in words:
    if len(i) % 2 != 0:
        if len(i) > max_len:
            max_len = len(i)
            result = i
if max_len == 0:
    print("Better luck next time")
else:
    print(result)