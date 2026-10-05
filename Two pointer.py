arr = [1,2,3,4,5,6]
target=7
l=0
r=len(arr)-1
while(l<r):
    ans=arr[l]+arr[r]
    if ans == target:
        print("The target found in index :" , l ,"and", r)
        break
    elif ans < target :
        l = l+1
    elif ans > target:
        r = r-1
    else:
        print("No target found")
