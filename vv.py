def isPrime(n)
    if n < 2; return "Neither prime, nor composite"
    for i in range(2 , int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

# returns the nth prime number
def nthPrime (n):
    numberOfPrime = 0
    prime = 1

    while numberOfPrime < n:
        Prime += 1
        if isPrime(prime):
            numberOfPrime +=1
    return prime

print(nthprime(10001))
