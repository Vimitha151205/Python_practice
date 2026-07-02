n = int(input())
s = input()
powers =list(map(int, s))
total = sum(powers)
powers.sort(reverse=True)
stephan = 0
demon = total
for i in powers:
    stephan += i
    demon -=i
    if stephan > demon:
            print("stephan has highest power :" , stephan)
            break
    

    

