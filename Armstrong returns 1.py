n = int(input())
temp = n
length = len(str(n))
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10
if sum == n:
    print(1)
else:
    print(sum)