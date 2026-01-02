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

def collatz(n: int):
    if n%2:
        return 3*n+1
    else:
        return n//2
    
s = ni()
numset = set([s])

prev = s
cur = 0
idx = 1
for i in range(2 * 10**6):
    idx += 1
    
    cur = collatz(prev)
    prev = cur
    
    if cur in numset:
        break
    else:
        numset.add(cur)
        
print(idx)