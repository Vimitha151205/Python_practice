n = int(input("Enter n: "))

count = 0

for num in range(1, n + 1):

    s = str(num)

    if any(d in "347" for d in s):
        continue

    if any(d in "2569" for d in s):
        count += 1

print("Answer:", count)
