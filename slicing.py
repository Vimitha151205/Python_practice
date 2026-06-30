str = input()
ans = ""

for i in range(1,len(str)):
     suffix = str[i:]
     if suffix > ans:
         ans = suffix
print(ans)
     
     
    
        
   