from collections import Counter


class SmallestPrimeFactors:
    def __init__(self, n):
        self.spf = list(range(n + 1))
        self.spf[0] = -1
        self.spf[1] = -1
        for i in range(2, int(n ** 0.5) + 1):
            if self.spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if self.spf[j] == j:
                        self.spf[j] = i

    def is_prime(self, x):
        return self.spf[x] == x

    def __traverse(self, x):
        if self.spf[x] == x:
            return [x]
        nxt = x // self.spf[x]
        return self.__traverse(nxt) + [self.spf[x]]

    def factor(self, x):
        if x < 2:
            return []
        return self.__traverse(x)


spf = SmallestPrimeFactors(1_000_000)
N = int(input())
ans = 0
for C in range(1, N):
    fac = Counter(spf.factor(N - C))
    tmp = 1
    for v in fac.values():
        tmp *= v + 1
    ans += tmp
print(ans)