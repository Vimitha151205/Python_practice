words = input()
vow = 0
cons = 0
for i in range(len(words)):
    if words[i] in "AEIOUaeiou":
        vow += 1
    else:
        cons += 1
print("Vowles are:" , vow)
print("Consonants are:" , cons)