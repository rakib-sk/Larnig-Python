isPrime = True
n = 9
i = 2

while i * i <= n:
    if n % i == 0:
        isPrime = False

    i += 1

print(isPrime)