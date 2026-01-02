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
p = list(li())

cnt = 0
i = 0
while i < n-1:
    if p[i] == i+1:
        p[i], p[i+1] = p[i+1], p[i]
        cnt += 1
        
    i += 1

        
if p[-1] == n:
    p[-1], p[-2] = p[-2], p[-1]
    cnt += 1
    
print(cnt)