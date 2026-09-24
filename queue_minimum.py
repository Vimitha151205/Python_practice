nums = list(map(int, input().split()))

count = 0
queue = nums[:]

while queue:
    minimum = min(queue)

    if queue[0] == minimum:
        queue.pop(0)
        count += 1
    else:
        first = queue.pop(0)
        queue.append(first)
        count += 1

print(count)
