from math import gcd
from functools import reduce
from collections import Counter

class Factorize:
    def __init__(self):
        self.primes = Counter()

    def add_target(self, n):
        for i in range(2, int(n**0.5)+1):
            while n%i==0:
                self.primes[i] += 1
                n //= i
            if not n:
                break
        if n>1:
            self.primes[n] += 1
    
    def get_result(self):
        return dict(self.primes)

N = int(input())
*A, = map(int, input().split())
def f():
    cnt = Counter()
    for i in A:
        ins = Factorize()
        ins.add_target(i)
        res = ins.get_result()
        for j in res.keys():
            cnt[j] += 1
            if cnt[j] >= 2:
                return False
    return True

cond1 = f()
cond2 = (reduce(gcd, A)==1)

if cond1:
    print("pairwise coprime")
elif cond2:
    print("setwise coprime")
else:
    print("not coprime")