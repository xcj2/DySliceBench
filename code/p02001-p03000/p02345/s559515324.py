import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

class SegTree():
    def __init__(self, node:int):
        self.n = node
        self.bit = len(bin(self.n-1)) - 2
        self.bottom = 2**self.bit
        
        if self.n == 1:
            self.bottom = 1
            
        self.segtree = [0]*(2*self.bottom-1)
        
        
    def fill(self, n:int):
        self.segtree = [n]*(2*self.bottom-1)
        
    def update(self, idx:int, x:int):
        idx += (self.bottom-1)
        self.segtree[idx] = x
        while idx > 0:
            k = (idx-1) >> 1
            self.segtree[k] = min(self.segtree[2*k+1],
                                  self.segtree[2*k+2])
            idx = k
            
            
    def find(self, left:int, right:int, idx:int, l:int, r:int):
        if left <= l and r <= right:
            return self.segtree[idx]

        elif l >= right or r <= left:
            return 10**10
        
        else:
            return min(self.find(left, right, 2*idx+1, l, (l+r)//2),
                       self.find(left, right, 2*idx+2, (l+r)//2, r))
        
            
n,q = li()
com = []
xy = []
for _ in range(q):
    c,x,y = li()
    com.append(c)
    xy.append((x, y))
    
segtree = SegTree(n)
segtree.fill(2**31-1)
    
for c, (x,y) in zip(com, xy):
    if c == 0:
        segtree.update(x, y)
        
    else:
        print(segtree.find(x, y+1, 0, 0, segtree.bottom))


