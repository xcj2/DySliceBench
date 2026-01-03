import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

x,y = li()

costs = [(1,1,0), (-1,1,1), (1,-1,1), (-1,-1,2)]
cands = []

for dx,dy,cost in costs:
    if dy*y - dx*x >= 0:
        cands.append(dy*y - dx*x + cost)
        
print(min(cands))