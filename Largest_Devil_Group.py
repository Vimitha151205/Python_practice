s = input()
start = 0
max_len = 0
for i in range(len(s)):
    if s[i] == '@' or s[i] == '$':
        group = s[start:i+1]
        if len(group) > max_len:
            max_len = len(group)
        start = i+1
group =s[i:]
if len(group) > max_len:
    max_len = len(group)
print(max_len)
        


 

        
    
    
        
      
    