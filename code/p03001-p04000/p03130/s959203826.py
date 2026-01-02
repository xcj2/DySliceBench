import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**8) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

cnt = [0]*4
for _ in range(3):
    a,b = li_()
    cnt[a] += 1
    cnt[b] += 1
    
if max(cnt) == 2:
    print('YES')
else:
    print('NO')