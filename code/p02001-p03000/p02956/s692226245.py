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

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n = int(input())
xyi = [[int(i) for i in readline().split()]+[j] for j in range(n)]
#xyi = []
#for i in range(n):
#    a = [int(i) for i in readline().split()]
#    xyi.append(a+[i])

#dame_x = [0]*n
#dame_y = [0]*n
#dame_xy = [0]*n

ABi = [0]*n
CDi = [0]*n

MOD = 998244353

sxyi = sorted(xyi, key = lambda x: x[1])
zaatu = [0]*n
for j in range(n): zaatu[sxyi[j][2]] = j
for j, (x,y,i) in enumerate(sxyi):
    ABi[i] = n-j-1
    CDi[i] = j

pow2 = [1]*(n+1)
for i in range(n):
    pow2[i+1] = pow2[i]*2%MOD


xyi.sort()
#print(pow2)

bit = BIT(n)

ans = n*(pow2[n]-1)%MOD
for j, (x,y,i) in enumerate(xyi):
    AB = ABi[i]
    CD = CDi[i]
    BC = j
    AD = n-j-1
    c = bit.sum(zaatu[i])
    C = c
    B = j-c
#    print(AB-B,B,C,CD-C)
    ans -= pow2[AB]-1 + pow2[CD]-1 
    ans -= pow2[BC]-1 + pow2[AD]-1
    ans += pow2[C]-1 + pow2[CD-C]-1 + pow2[B]-1 + pow2[AB-B]-1

    bit.add(zaatu[i],1)
        

        


print(ans%MOD)    






