k = int(input())
n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
mins =[]
for i in range(n-k+1):
    sub = arr[i:i+k]
    mins.append(min(sub))
print(max(mins))
    