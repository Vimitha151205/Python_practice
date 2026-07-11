n = int(input())
words = input().strip()
str = words.split()
if n == 0:
    print(str[0].lower() + ''.join(i.capitalize() for i in str[1:]))
else:
    print('_'.join(i.lower() for i in str))
