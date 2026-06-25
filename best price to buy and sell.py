n = int(input())  
price = list(map(int, input().split()))

min_price = float('inf')
max_profit = 0

for i in range(n):
    if price[i] < min_price:
        min_price = price[i]
    else:
        profit = price[i] - min_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)