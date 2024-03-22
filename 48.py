tot = 405071317
for i in range(11, 1001):
    temp = i
    for j in range(2, i+1):
        temp *= i
        if (len(str(temp)) >= 11):
            temp = int(str(temp)[-11:])
    tot += temp
print(tot)
