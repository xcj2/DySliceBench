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

n,m = li()
py = []
for _ in range(m):
    py.append(list(li()))
    
towns = [[] for _ in range(n+1)]
table = [{} for _ in range(n+1)]
for p,y in py:
    towns[p].append(y)
    
for i in range(n+1):
    if len(towns[i]) > 0:
        towns[i].sort()
        
for i in range(n+1):
    if len(towns[i]) > 0:
        for j, tj in enumerate(towns[i]):
            table[i].update({tj: j+1})
            
for p,y in py:
    print(str(p).zfill(6) + str(table[p][y]).zfill(6))