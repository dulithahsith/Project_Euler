ones = [3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [0, 6, 6, 5, 5, 5, 7, 6, 6]
hundreds = [0, 13, 13, 15, 14, 14, 13, 15, 15, 14]
tot = 0

for i in hundreds:
    for j in tens:
        for k in ones:
            tot += i+j+k
        if j == 0:
            tot += i*9 + 6+6+8+7+7+9+8+9+8
    for j in tens:
        tot += i+j
    tot += 3
for i in hundreds:
    tot += i
tot -= 27
print(tot)
