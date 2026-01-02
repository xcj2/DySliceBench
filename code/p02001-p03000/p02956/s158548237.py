# coding: utf-8
# Your code here!
"""
Binary indexed tree
0-indexed, 関数は閉区間
0からの区間加算、1点更新
"""
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
# http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3791366
###########################################

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n = int(input())
xyi = [[int(i) for i in readline().split()]+[j] for j in range(n)]
#xyi = []
#for i in range(n):
#    a = [int(i) for i in readline().split()]
#    xyi.append(a+[i])

dame_x = [0]*n
dame_y = [0]*n
dame_xy = [0]*n

MOD = 998244353

sxyi = sorted(xyi, key = lambda x: x[1]) # zaatu の逆写像
modosu = [i for x,y,i in sxyi]
zaatu = [0]*n
for j,zj in enumerate(modosu):
    zaatu[zj] = j

pow2 = [1]*(n+1)
for i in range(n):
    pow2[i+1] = pow2[i]*2%MOD

for j, (x,y,i) in enumerate(sxyi):
    dame_y[i] = pow2[j]-1 + pow2[n-j-1]-1

xyi.sort()
#print(pow2)

bit = BIT(n)
for j, (x,y,i) in enumerate(xyi):
    dame_x[i] = pow2[j] -1 + pow2[n-j-1]-1
    c = bit.sum(zaatu[i])
    dame_xy[i] += pow2[c]-1 + pow2[j-c]-1
    bit.add(zaatu[i],1)
        
bit = BIT(n)
for j, (x,y,i) in enumerate(reversed(xyi)):
    c = bit.sum(zaatu[i])
    dame_xy[i] += pow2[c]-1 + pow2[j-c]-1
    bit.add(zaatu[i],1)
        
        
#print(dame_x,"\n",dame_y,"\n",dame_xy)

ans = n*(pow2[n]-1)%MOD
for dx,dy,dxy in zip(dame_x,dame_y,dame_xy):
    ans += - dx - dy + dxy


print(ans%MOD)    






