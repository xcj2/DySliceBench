from collections import Counter
class Prime:
    def __init__(self, N):
        smallestPrime = [i for i in range(N + 1)]

        for i in range(2, N + 1):
            if smallestPrime[i] != i:
                continue
            for p in range(i * 2, N + 1, i):
                if smallestPrime[p] == p:
                    smallestPrime[p] = i

        self.smallestPrime = smallestPrime

    def isPrime(self, n):
        return n > 1 and self.smallestPrime[n] == n

    def factorization(self, n):
        ret = Counter()
        while n > 1:
            p = self.smallestPrime[n]
            ret[p] += 1
            n //= p
        return ret

N = int(input())
prime = Prime(N + 100)

ans = 0
for c in range(1, N):
    cnt = 1
    for c in prime.factorization(N - c).values():
        cnt *= c + 1
    ans += cnt
print(ans)
