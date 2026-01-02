import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement
from functools import reduce
from math import sin, cos, tan, asin, acos, atan, degrees, radians

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def lcm(x,y):
    return x*y//gcd(x,y)
def lgcd(l):
    return reduce(gcd,l)
def llcm(l):
    return reduce(lcm,l)
def powmod(n,i,mod):
    return pow(n,mod-1+i,mod) if i<0 else pow(n,i,mod)
def div2(x):
    return x.bit_length()
def div10(x):
    return len(str(x))-(x==0)
def perm(n,mod=None):
    ans = 1
    for i in range(1,n+1):
        ans *= i
        if mod!=None:
            ans %= mod
    return ans
def intput():
    return int(input())
def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def ilint():
    return int(input()), list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)
def ston(c, c0='a'):
    return ord(c)-ord(c0)
def ntos(x, c0='a'):
    return chr(x+ord(c0))
class counter(dict):
    def __init__(self, *args):
        super().__init__(args)
    def add(self,x,d=1):
        self.setdefault(x,0)
        self[x] += d
class comb():
    def __init__(self, n, mod=None):
        self.l = [1]
        self.n = n
        self.mod = mod
    def get(self,k):
        l,n,mod = self.l, self.n, self.mod
        k = n-k if k>n//2 else k
        while len(l)<=k:
            i = len(l)
            l.append(l[i-1]*(n+1-i)//i if mod==None else (l[i-1]*(n+1-i)*powmod(i,-1,mod))%mod)
        return l[k]

class SegmentTree():
    
    # 目的関数！！
    def func(self,x,y):
        return x+y
    
    # インデックスは0-start
    # 初期化（配列と初期値）
    def __init__(self, array, initial_value=0):
        
        self.n = len(array)
        self.init_val = initial_value
        self.num = 2**(self.n-1).bit_length()
        self.seg = [self.init_val]*2*self.num
        
        for i in range(self.n):
            self.seg[i+self.num-1] = array[i]
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.func(self.seg[2*i+1],self.seg[2*i+2]) 
    
    # k番目の要素をxに変更
    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.func(self.seg[2*k+1],self.seg[2*k+2])
    
    # k番目の要素にxを追加
    def add(self,k,x):
        k_tmp = k+self.num-1
        x_tmp = self.seg[k_tmp]+x
        self.update(k,x_tmp)
    
    # [p,q]に対するクエリを処理
    def query(self,p,q):
        q += 1
        if q<=p:
            return self.init_val
        p += self.num-1
        q += self.num-2
        res = self.init_val
        while q-p>1:
            if p&1 == 0:
                res = self.func(res,self.seg[p])
            if q&1 == 1:
                res = self.func(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.func(res,self.seg[p])
        else:
            res = self.func(self.func(res,self.seg[p]),self.seg[q])
        return res
    
    # もとの配列を出力
    def result(self):
        return self.seg[self.num-1:self.n+self.num-1]
N,K = mint()
A = lint()
T = [0]*2001
for a in A:
    T[a] += 1
t = SegmentTree(T)
s = SegmentTree([0]*2001)
ans = 0
for a in A:
    t.add(a,-1)
    ans += t.query(0,a-1)*K*(K+1)//2
    ans %= MOD
    ans += s.query(0,a-1)*K*(K-1)//2
    ans %= MOD
    s.add(a,1)
print(ans)