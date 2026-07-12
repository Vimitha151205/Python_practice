\\ Method 1 

*/n = input("Enter a number:").split()
num = set()
for i in range(len(n)):
    num.add(n[i])
print(num) /*

\\ Method 2

n = set(map(input("Enter a number:").split()))
print("Unique numbers are:\n" , n)
break

    
    
