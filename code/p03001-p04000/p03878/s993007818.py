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

MOD = 10**9+7

devices = []

n = ni()
for _ in range(n):
    a = ni()
    devices.append((a, 1))
    
for _ in range(n):
    b = ni()
    devices.append((b, -1))
    
devices.sort()

pc = [0,0]

ans = 1
for point, typ in devices:
    if typ == 1 and pc[1] > 0:
        ans = (ans * pc[1]) % MOD
        pc[1] -= 1
        
    elif typ == 1:
        pc[0] += 1
        
    elif typ == -1 and pc[0] > 0:
        ans = (ans * pc[0]) % MOD
        pc[0] -= 1
        
    elif typ == -1:
        pc[1] += 1
        
print(ans)