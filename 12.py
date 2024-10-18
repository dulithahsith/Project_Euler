def is_prime(num):
    temp = 0
    for i in range(2, int(num**0.5)+1):
        if (num % i == 0):
            temp = 1
            return False
            break
    if (temp == 0):
        return True


def is_divisible(num):
    c = 0
    for i in range(2, int(num**0.5)+1):
        if (num % i == 0):
            c += 1
    if (c % 2 == 1):
        return 2*c+1
    else:
        return 2*c+2


def generate_prime(count):
    primes = []
    for i in range(2, count):
        if (is_prime(i)):
            primes.append(i)
    return primes


primes = generate_prime(1000000)
print("Okay")
for i in range(1000000):
    if (i in primes):
        continue
    if (is_divisible(i) > 500):
        print(i)
