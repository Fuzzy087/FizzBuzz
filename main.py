
primes = []

for possiblePrime in range(2, 100):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    if isPrime:
        primes.append(possiblePrime)

print(primes)

for num in range(1, 100):
    if num in primes:
        print(num, "Prime")
    elif num % 5 == 0 and num % 3 == 0:
        print (num, "FizzBuzz")
    elif num % 5 == 0 and num % 3 != 0:
        print (num, "Fizz")
    elif num % 5 != 0 and num % 3 == 0:
        print (num, "Buzz")
    else:
        print(num)