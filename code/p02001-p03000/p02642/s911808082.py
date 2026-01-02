from itertools import combinations
from collections import Counter
class Osa_k:
    def __init__(self, n_max):
        self.n_max = n_max
        self.min_factor = min_factor = list(range(n_max + 1))
        min_factor[2::2] = [2] * (n_max // 2)
        min_factor[3::6] = [3] * ((n_max + 3) // 6)
        for i in range(5, int(n_max ** .5) + 1, 2):
            if min_factor[i] == i:
                for j in range(i*i, n_max + 1, i):
                    if min_factor[j] == j:
                        min_factor[j] = i

    def __call__(self, n):
        min_factor = self.min_factor
        n_twoes = (n & -n).bit_length() - 1
        res = [2] * n_twoes
        n >>= n_twoes
        resappend = res.append
        while n > 1:
            p = min_factor[n]
            resappend(p)
            n //= p
        return res
    
    def div(self, n):
        factors = self.__call__(n)
        res = {1, n}
        for i in range(1, len(factors)):
            for j in combinations(factors, i):
                r = 1
                for p in j:r *= p
                res |= {r}
        return res

if __name__ == "__main__":
    n, *a = map(int, open(0).read().split())
    b, c = set(a), Counter(a)
    P = Osa_k(10**6)
    cnt = 0
    for i in b:
        if c[i] > 1:continue
        for d in P.div(i):
            if d != i and d in b:break
        else:cnt += 1
    print(1 if n == 1 else cnt)