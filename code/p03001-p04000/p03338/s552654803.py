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

ans = 0
for i in range(n):
    set1 = set(s[:i])
    set2 = set(s[i:])
    ans = max(ans, len(set1&set2))
    
print(ans)