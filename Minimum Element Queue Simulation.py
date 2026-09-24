nums = [3,4,-1]
count = 0
while nums:
    minimum = min(nums)
    if nums[0]==minimum:
        nums.pop(0)
        count +=1
    else:
        first = nums.pop(0)
        nums.append(first)
        count +=1
print(count)
                         
