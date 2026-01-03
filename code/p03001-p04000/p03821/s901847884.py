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

n = ni()
a = []
b = []
for _ in range(n):
    ai,bi = li()
    a.append(ai)
    b.append(bi)
    
a = a[::-1]
b = b[::-1]

ans = 0

for ai,bi in zip(a,b):
    if (ans + ai) % bi == 0:
        continue
    
    else:
        ans += (bi - (ans+ai)%bi)
    
print(ans)