ones = [3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [0, 6, 6, 5, 5, 5, 7, 6, 6]
hundreds = [0, 7, 7, 7, 7, 7, 7, 7, 7, 7]
tot = 0

for i in hundreds:
    for j in tens:
        for k in ones:
            tot += i+j+k
        if j == 0:
            tot += 6+6+8+7+7+9+8
print(tot)
