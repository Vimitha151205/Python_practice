i = int(input())
j = int(input())
k = int(input())
total = 0

for x in range(i,j+1):
    total +=x
for x in range(j-1,k-1,-1):
        total +=x
print(total)