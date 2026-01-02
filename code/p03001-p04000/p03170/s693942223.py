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

n,k = li()
a = list(li())

LOSE = -1
WIN = 1

dp = [0]*(k+1)
for i in range(a[0]):
    dp[i] = LOSE
    
for i in range(a[0], k+1):
    lost = True
    for ai in a:
        if i-ai < 0:
            continue
        
        if dp[i-ai] == LOSE:
            lost = False
            
    dp[i] = LOSE if lost else WIN
    
print('First') if dp[k] == WIN else print('Second')