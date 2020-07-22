def genPrimes():
    numbers = [1]
    i = 1
    while True:
        i += 1
        numbers.append(i)
        perfDivisions = 0
        for x in numbers:
            if i % x == 0:
                perfDivisions += 1
        if perfDivisions < 3:
            yield i

primes = genPrimes()

print(primes.__next__())

print(primes.__next__())

print(primes.__next__())

print(primes.__next__())

print(primes.__next__())

print(primes.__next__())