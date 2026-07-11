str = input().split()
total = 0
length = len(str)
for i in str:
    total +=ord(i)
print(total/length)