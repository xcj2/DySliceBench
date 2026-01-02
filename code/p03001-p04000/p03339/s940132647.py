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
s = lc()

le = 0
lw = 0
re = s[1:].count("E")
rw = s[1:].count("W")

ans = lw + re

for i in range(1,n):
    if s[i-1] == "E":
        le += 1
    else:
        lw += 1
        
    if s[i] == "E":
        re -= 1
    else:
        rw -= 1
        
    ans = min(ans, lw+re)

print(ans)