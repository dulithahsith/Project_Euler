lim = 1000000
x = [1]*(lim+1)
x[0] = x[1] = 0
primes = []
for i in range(2, lim):
    if x[i]:
        primes.append(i)
        for j in range(i*i, lim+1, i):
            x[j] = 0

max_len = 0
max_val = 0
for i in range(len(primes)):
    tot = 0
    for j in range(i, len(primes)):
        tot += primes[j]
        if (tot > lim):
            break
        if (x[tot] and max_len < j-i+1):
            max_len = j-i+1
            max_val = tot
print(max_val)
print(max_len)
