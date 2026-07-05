str = input()
answer = []
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        answer.append(str[i:j])
print(sorted(answer)[-1])
