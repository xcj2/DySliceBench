import sys
input = sys.stdin.readline
from collections import *

class BIT:
    #n:要素数
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    
    #i番目(0-indexed)の値にxを足す
    def add(self, i, x):
        i += 1
        
        while i<=self.n:
            self.bit[i] += x
            i += i&(-i)
    
    #0からi番目までの値の和を求める
    def acc(self, i):
        i += 1
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s
        
def compress(l):
    l = list(set(l))
    l.sort()
    idx = defaultdict(int)
    
    for i in range(len(l)):
        idx[l[i]] = i
    
    return idx

def judge(x):
    l = []
    
    for ai in a:
        if ai>=x:
            l.append(1)
        else:
            l.append(-1)
    
    acc = [0]*(N+1)
    
    for i in range(N):
        acc[i+1] = acc[i]+l[i]
    
    idx = compress(acc)
    bit = BIT(len(idx.keys()))
    cnt = 0
    
    for i in range(N+1):
        cnt += bit.acc(idx[acc[i]])
        bit.add(idx[acc[i]], 1)

    return cnt>=(N*(N+1)//2+1)//2
    
def binary_search():
    l, r = 0, max(a)
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            l = m+1
        else:
            r = m-1
    
    return r

N = int(input())
a = list(map(int, input().split()))
print(binary_search())