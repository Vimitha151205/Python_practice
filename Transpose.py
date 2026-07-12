rows = int(input())
cols = int(input())

Matrix = []

for i in range(rows):
    arr =list(map(int, input().split()))
    Matrix.append(arr)
print("------output------")

    
for i in range(cols):
    for j in range(rows):
        print(Matrix[j][i], end =" ") 
    print()       
        