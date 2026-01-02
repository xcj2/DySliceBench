class BIT_dinamic: #0-indexed
    def __init__(self, n):
        self.tree = {}
        self.MAX = n
    def get_sum(self, i): #a_0 + ... + a_{i} #閉区間
        s = 0; i += 1
        while i > 0:
            if i in self.tree:
                s += self.tree[i]
            i -= i & -i
        return s
    def query(self,l,r): #a_l + ... + a_r 閉区間
        return self.get_sum(r) - self.get_sum(l-1) 
    def add(self, i, x):
        i += 1
        while i <= self.MAX:
            if i in self.tree:
                self.tree[i] += x
            else:
                self.tree[i] = x
            i += i & -i

   
###########################################
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

n = int(input())
a = [int(i) for i in readline().split()]

sA = sorted(a)
# def zaatu(x): return bisect_left(sA, x) #xの圧縮先
# def modosu(i): return sA[i]  # 逆写像

b = BIT_dinamic(n)

from bisect import *
ans = 0
for i,ai in enumerate(a):
    j = bisect_left(sA, ai)
    ans += i - b.get_sum(j)
    b.add(j,1)

print(ans)

