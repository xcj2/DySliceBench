import sys
## io
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))
## dp
INIT_VAL = 0
MD2 = lambda d1,d2: [[INIT_VAL]*d2 for _ in range(d1)]
MD3 = lambda d1,d2,d3: [MD2(d2,d3) for _ in range(d1)]
## math
DIVC = lambda x,y: -(-x//y)
DIVF = lambda x,y: x//y
from itertools import accumulate as acc

class PrimeOptimizer:
    def __init__(self, MAX_NUM=10**3):
        """MAX_NUM以下の素数テーブルを生成する。
        生成した素数テーブルはprime_factorizationで使用する。
        """
        is_prime = [True] * MAX_NUM
        is_prime[0] = False
        is_prime[1] = False
        primes = []
        for i in range(MAX_NUM):
            if is_prime[i]:
                primes.append(i)
                for j in range(2*i, MAX_NUM, i):
                    is_prime[j] = False
        self.primes = primes

    def prime_factorization(self, x):
        """xを素因数分解する。
        分解先の素数はself.primesを利用する。
        @param x (int): 分解対象の正整数
        @return res (dict): key = 素数、value = 素数の数で構成される辞書
        """
        res = {}
        for prime in self.primes:
            while x % prime == 0:
                if not prime in res:
                    res[prime] = 0
                res[prime] += 1
                x //= prime
        if x > 1:
            res[x] = 1
        return res

def main():
    q = II()
    lr = [MII() for _ in range(q)]
    pm = PrimeOptimizer(MAX_NUM=10**5)
    prims = set(pm.primes)
    like_2017 = [0]*10**5
    for n in range(1,10**5):
        if n in prims and (n+1)//2 in prims:
            like_2017[n] = 1
    acc_like_2017 = list(acc(like_2017))
    for l,r in lr:
        print(acc_like_2017[r]-acc_like_2017[l-1])

if __name__ == '__main__':
    main()