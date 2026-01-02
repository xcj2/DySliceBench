import sys
import heapq
import re
from itertools import permutations
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from math import factorial, sqrt, ceil, gcd
from functools import lru_cache, reduce
from decimal import Decimal
from operator import mul

INF = 1 << 60
MOD = 1000000007
sys.setrecursionlimit(10 ** 7)


# UnionFind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# ダイクストラ
def dijkstra_heap(s, edge, n):
    #始点sから各頂点への最短距離
    d = [10**20] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# 組合せnCr
def combinations_count(n, r):
    if n < r:
        return 0
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

# 2数の最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

# リストの要素の最小公倍数
def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

# リストの要素の最大公約数
def gcd_list(numbers):
    return reduce(gcd, numbers)

# 素数判定
def is_prime(n):
    if n <= 1:
        return False
    p = 2
    while True:
        if p ** 2 > n:
            break
        if n % p == 0:
            return False
        p += 1
    return True


# limit以下の素数を列挙
def eratosthenes(limit):
    A = [i for i in range(2, limit+1)]
    P = []

    while True:
        prime = min(A)
        
        if prime > sqrt(limit):
            break
            
        P.append(prime)
            
        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1
            
    for a in A:
        P.append(a)
            
    return P

# 同じものを含む順列
def permutation_with_duplicates(L):

    if L == []:
        return [[]]

    else:
        ret = []

        # set（集合）型で重複を削除、ソート
        S = sorted(set(L))

        for i in S:

            data = L[:]
            data.remove(i)

            for j in permutation_with_duplicates(data):
                ret.append([i] + j)

        return ret

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]



# ここから書き始める
MAX_N = 10**6

fact = [1]
fact_inv = [0]*(MAX_N+4)
for i in range(MAX_N+3):
    fact.append(fact[-1]*(i+1)%MOD)

fact_inv[-1] = pow(fact[-1],MOD-2,MOD)
for i in range(MAX_N+2,-1,-1):
    fact_inv[i] = fact_inv[i+1]*(i+1)%MOD


def mod_comb_k(n,k,mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] %mod


x, y = map(int, input().split())
ans = 0
for i in range(x + 1):
    cnt1 = i
    if (x - cnt1) % 2 != 0 or y - 2 * cnt1 != (x - cnt1) // 2:
        continue
    cnt2 = (x - cnt1) // 2
    ans += mod_comb_k(cnt1 + cnt2, cnt1, MOD)
print(ans % MOD)