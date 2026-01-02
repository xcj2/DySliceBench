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

n = ni()

ans = 0
for i in range(1,n+1,2):
    temp = 0
    for j in range(1,i+1):
        if i%j == 0:
            temp += 1
            
    if temp == 8:
        ans += 1
        
print(ans)