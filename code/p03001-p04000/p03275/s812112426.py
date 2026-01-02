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

# 転倒数を求めるためのBIT
class BIT(object):
    def __init__(self, size):
        self.size = size+1
        self.bitree = [0]*self.size
        
    def addval(self, idx:int, val:int):
        while idx < self.size:
            self.bitree[idx] += val
            idx += idx&(-idx)
            
    def getsum(self, idx:int):
        ret = 0
        while idx > 0:
            ret += self.bitree[idx]
            idx -= idx&(-idx)
            
        return ret
    
    def reset(self):
        self.bitree = [0]*self.size
        
# 二分探索のための関数
def findInv(arr:list, med:int):
    arrbin = [-1 if ai < med else 1 for ai in arr]
    arrcum = [0] + list(accumulate(arrbin))
    arrcummin = abs(min(arrcum))
    arrcumpos = [arrcum_i + arrcummin + 1 for arrcum_i in arrcum]
    
    bitree = BIT(max(arrcumpos))
    inv = 0
    for i,ai in enumerate(arrcumpos):
        inv += (i - bitree.getsum(ai))
        bitree.addval(ai, 1)
        
    return inv

# 二分探索
def binsearch(arr:list):
    low = 0
    high = max(arr) + 1
    n = len(arr)
    threshould = n*(n+1)//4
    
    while high-low > 1:
        mid = (high+low) // 2

        if findInv(arr, mid) <= threshould:
            low = mid
            
        else:
            high = mid
            
    return low        

n = ni()
a = list(li())

print(binsearch(a))