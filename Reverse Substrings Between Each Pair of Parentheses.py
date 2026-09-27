s = input("Enter string: ")

stack = []

for ch in s:

    if ch == '(':
        stack.append(ch)

    elif ch == ')':
        temp = []

        while stack[-1] != '(':
            temp.append(stack.pop())

        stack.pop()

        stack.extend(temp)

    else:
        stack.append(ch)

result = ''.join(stack)

print("Result:", result)
