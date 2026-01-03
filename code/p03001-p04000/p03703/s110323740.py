import sys
input = sys.stdin.readline
from collections import defaultdict
 
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
    
    #0からi番目までの値の和を求める
    def acc(self, i):
        i += 1
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s

N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
l = [0]
acc = 0

for i in range(N):
    acc += a[i]
    l.append(acc-K*(i+1))

idx = compress(l)
bit = BIT(len(list(idx.keys())))
bit.add(idx[0], 1)
ans = 0
acc = 0

for i in range(N):
    acc += a[i]
    ans += bit.acc(idx[acc-K*(i+1)])
    bit.add(idx[acc-K*(i+1)], 1)
    
print(ans)