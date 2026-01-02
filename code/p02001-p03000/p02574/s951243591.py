def examA():
    D,T,S = LI()
    if (D-1)//S<T:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
    return

def examB():
    S = SI()
    T = SI()
    s = len(S)
    t = len(T)
    ans = t
    for i in range(s-t+1):
        cnt = 0
        for j in range(t):
            if S[i+j]!=T[j]:
                cnt += 1
        ans = min(ans,cnt)

    print(ans)
    return

def examC():
    N = I()
    A = LI()
    S = sum(A)
    cnt = 0
    for a in A:
        cnt += (S-a)*a
        cnt %= mod
    ans = cnt * pow(2,mod-2,mod) % mod
    print(ans)
    return

def examD():
    class UnionFind():
        def __init__(self, n):
            self.parent = [-1 for _ in range(n)]
            # 正==子: 根の頂点番号 / 負==根: 連結頂点数

        def reset(self):
            self.parent = [-1] * len(self.parent)

        def find(self, x):
            # 要素xが属するグループの根を返す
            if self.parent[x] < 0:
                return x
            else:
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        def unite(self, x, y):
            # 要素xが属するグループと要素yが属するグループとを併合する
            x, y = self.find(x), self.find(y)
            if x == y:
                return False
            else:
                if self.size(x) < self.size(y):
                    x, y = y, x
                self.parent[x] += self.parent[y]
                self.parent[y] = x

        def same(self, x, y):
            # 要素x, yが同じグループに属するかどうかを返す
            return self.find(x) == self.find(y)

        def size(self, x):
            # 要素xが属するグループのサイズ（要素数）を返す
            x = self.find(x)
            return -self.parent[x]

        def is_root(self, x):
            # 要素の根をリストで返す
            return self.parent[x] < 0

        def roots(self):
            # すべての根の要素をリストで返す
            return [i for i, x in enumerate(self.parent) if x < 0]

        def members(self, x):
            # 要素xが属するグループに属する要素をリストで返す
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def group_count(self):
            # グループの数を返す
            return len(self.roots())

        def all_group_members(self):
            # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
            return {r: self.members(r) for r in self.roots()}
    N, M = LI()
    uf = UnionFind(N)
    for _ in range(M):
        a, b = LI()
        a -= 1; b -= 1
        uf.unite(a,b)
    cnt = 0
    for i in range(N):
        cnt = max(cnt,uf.size(i))

    ans = cnt
    print(ans)
    return

def examE():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x

    def primes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    N = I()
    A = LI()
    cur = A[0]
    for i in range(1,N):
        cur = gcd(cur,A[i])
        if cur==1:
            break
    if cur!=1:
        print("not coprime")
        return

    n = max(A)

    P = primes(n)

    #print(P)

    D = [False]*(n+1)
    for a in A:
        if a==1:
            continue
        if D[a]:
            print("setwise coprime")
            return
        D[a] = True

    for p in P:
        flag = False
        cur = 1
        while (cur * p <= n):
            if D[cur*p]:
                if flag:
                    print("setwise coprime")
                    return
                flag = True

            cur += 1

    print("pairwise coprime")
    return

def examF():

    ans = 0
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""