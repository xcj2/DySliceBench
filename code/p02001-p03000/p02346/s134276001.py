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

class BIT(object):
    def __init__(self, size: int):
        self.bitree = [0]*(size+1)
        
    def setval(self, idx:int, val:int):
        tree = self.bitree
        nex_idx = idx+1
        
        while nex_idx < len(tree):
            tree[nex_idx] += val
            nex_idx += nex_idx & -nex_idx
            
    def getsum(self, idx: int):
        tree, result = self.bitree, 0
        nex_idx = idx+1
        
        while nex_idx:
            result += tree[nex_idx]
            nex_idx -= nex_idx & -nex_idx
            
        return result
    
n,q = li()
bitree = BIT(n)

for _ in range(q):
    com, x, y = li()
    if com == 0:
        bitree.setval(x-1, y)
    else:
        print(bitree.getsum(y-1) - bitree.getsum(x-2))
        
