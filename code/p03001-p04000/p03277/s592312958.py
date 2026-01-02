import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
        
    def node_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
            
        return s
    
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += (i & -i)
            
    def reset(self):
        self.tree = [0] * (self.size + 1)
        
        
n = ni()
a = list(li())

t = n*(n+1) // 4
alt = sorted(set(a))

l,r = 0, len(alt) - 1
bitree = BIT(n*2)

while l <= r:
    m = (l+r) // 2
    am = alt[m]
    acc = accumulate(1 if ai-am >= 0 else -1 for ai in a)
    bitree.add(n,1)
    right_order = 0
    
    for p in acc:
        p += n
        right_order += bitree.node_sum(p)
        bitree.add(p, 1)
        
    if right_order >= t:
        l = m+1
    else:
        r = m-1
        
    bitree.reset()
    
print(alt[r])