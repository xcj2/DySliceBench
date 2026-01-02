# https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion から
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
from itertools import accumulate

def bsearch(target, min_i, max_i, func):
    # func(index) <= target < func(index+1) となるindexを返す
    if func(max_i) <= target:
        return max_i
    if target < func(min_i):
        return None
    index = (max_i + min_i)//2
    while True:
        if max_i - min_i <= 1:
            return min_i
        if func(index) <= target:
            index, min_i = (index + max_i)//2, index
            continue
        index, max_i = (index + min_i)//2, index

N, = map(int, input().split())
As = list(map(int, input().split()))
mna, mxa = min(As), max(As)

def tento(xs):
    bit = Bit(max(xs)+1)
    ans = 0
    for i, p in enumerate(xs):
        ans += bit.sum(p)
        bit.add(p, 1)
        #print(p, ans)
    #print(xs, ans)
    return ans

def f(x):
    Bs = [0] + list(accumulate(map(lambda a: 1 if a>=x else -1, As)))
    mn = min(Bs)
    Bs = list(map(lambda x : x - mn + 1, Bs))
    return -tento(Bs)

M = (N*(N+1))//2
print(bsearch((-M//2) , mna, mxa, f))
