def sieve():
    L = 50000
    primes = []
    isPrime = [ True for _ in range(L) ]
    for i in range(2, L):
        if isPrime[i]:
            primes.append(i)
            for j in range(i*i, L, i):
                isPrime[j] = False
    return primes

def isConsecutivePrime(num, idx, primes):
    p = 0
    while True:
        p += primes[idx]
        if p == num:
            return True
        if p > num:
            return False
        idx += 1

def countConsecutivePrimes(num, primes):
    count = 0
    for i in range(len(primes)):
        if isConsecutivePrime(num, i, primes):
            count += 1
    return count

if __name__ == '__main__':
    primes = sieve()
    while True:
        num = int(input())
        if num == 0:
            break
        print(countConsecutivePrimes(num, primes))
