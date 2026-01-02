# coding: utf-8
# Your code here!

class BIT: #0-indexed
    def __init__(self, n):
        self.tree = [0]*(n+1)
        self.tree[0] = None
#        self.element = [0]*(n+1)
    def sum(self, i): #a_0 + ... + a_{i} #閉区間
        s = 0; i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def range(self,l,r): #a_l + ... + a_r 閉区間
        return sum(r) - sum(l-1) 
    def add(self, i, x):
        i += 1
        while i <= n:
            self.tree[i] += x
            i += i & -i
        # self.element[i] += x
    #def get(self,i): return element[i]        
     
###########################################
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意
 
#n = int(input())
n,k = [int(i) for i in readline().split()]
a = [int(i) for i in readline().split()]
 
sA = sorted(a)
# def zaatu(x): return bisect_left(sA, x) #xの圧縮先
# def modosu(i): return sA[i]  # 逆写像
 
b = BIT(n)
 
from bisect import *
res = [0]*n
for i,ai in enumerate(a):
    j = bisect_left(sA, ai)
    res[i] = i - b.sum(j)
    b.add(j,1)
 
#print(res)

MOD = 10**9 + 7
ans = 0
for i,ai in enumerate(a):
    ans += k*res[i]
    ans %= MOD
    j = bisect_left(sA, ai)
    ans += (k*(k-1)//2%MOD)*(n - b.sum(j))
    ans %= MOD
    

print(ans)











