nums = list(map(int, input("Enter numbers: ").split()))

n = len(nums)

total = sum(nums)

f = 0

for i in range(n):
    f += i * nums[i]

maximum = f

for k in range(1, n):
    f = f + total - n * nums[n - k]

    maximum = max(maximum, f)

print("Maximum Rotate Function:", maximum)
