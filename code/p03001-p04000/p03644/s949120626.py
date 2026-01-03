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

ans = 1
temp = 0
res = 0
for i in range(1,n+1):
    m = i
    temp = 0
    while m % 2 == 0:
        m //= 2
        temp += 1

    if temp > res:
        res = temp
        ans = i
    
print(ans)