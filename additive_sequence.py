num = input()

for i in range(1, len(num)):
    for j in range(i + 1, len(num)):

        first = num[:i]
        second = num[i:j]

        if len(first) > 1 and first[0] == '0':
            continue

        if len(second) > 1 and second[0] == '0':
            continue

        a = int(first)
        b = int(second)

        pos = j
        count = 2

        while pos < len(num):
            c = a + b
            c_str = str(c)

            if not num.startswith(c_str, pos):
                break

            pos += len(c_str)
            a = b
            b = c
            count += 1

        if pos == len(num) and count >= 3:
            print("true")
            break
    else:
        continue
    break
else:
    print("false")
