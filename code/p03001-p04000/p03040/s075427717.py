import sys
input = sys.stdin.readline
from collections import *

def compress(l):
    l = list(set(l))
    l.sort()
    idx = defaultdict(int)
    
    for i in range(len(l)):
        idx[l[i]] = i
    
    return idx
    
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
    
    #sum[0, i)
    def acc(self, i):
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s

Q = int(input())
que = []
vals = []

for _ in range(Q):
    l = list(map(int, input().split()))
    que.append(l)
    
    if len(l)==3:
        vals.append(l[1])

idx = compress(vals)
rev_idx = defaultdict(int)

for k, v in idx.items():
    rev_idx[v] = k
    
N = len(list(idx.keys()))
bit1 = BIT(N)
bit2 = BIT(N)
b_acc = 0
cnt = 0

for i in range(Q):
    if len(que[i])==3:
        a, b = que[i][1], que[i][2]
        b_acc += b
        bit1.add(idx[a], 1)
        bit2.add(idx[a], a)
        cnt += 1
    else:
        l, r = 0, N-1
        
        while l<=r:
            m = (l+r)//2
            
            if bit1.acc(m+1)>=(cnt+1)//2:
                r = m-1
            else:
                l = m+1
        
        x = l
        lsum = bit1.acc(x)*rev_idx[x]-bit2.acc(x)
        rsum = bit2.acc(N)-bit2.acc(x)-(bit1.acc(N)-bit1.acc(x))*rev_idx[x]
        print(rev_idx[x], lsum+rsum+b_acc)