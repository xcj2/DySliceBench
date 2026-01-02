from math import gcd
from functools import reduce
from collections import Counter


class Osa_k:
    def __init__(self, maximum):
        self.table = [-1] * (maximum+1)
        for i in range(2, maximum+1):
            if self.table[i] != -1:
                continue
            self.table[i] = i
            for k in range(i*i, maximum+1, i):
                if self.table[k] == -1:
                    self.table[k] = i

    def factorize(self, n):
        res = Counter()
        b = n
        while 1:
            if self.table[b] == -1:
                break
            res[self.table[b]] += 1
            b //= self.table[b]
        if b != 1:
            res[b] += 1
        return res


N = int(input())
*A, = map(int, input().split())
def f():
    cnt = Counter()
    ins = Osa_k(max(A))
    for i in A:
        res = ins.factorize(i)
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
