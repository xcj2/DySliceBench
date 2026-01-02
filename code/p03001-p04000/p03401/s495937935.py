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
a = [0] + list(li()) + [0]

sm = 0
for i in range(len(a)-1):
    sm += (abs(a[i+1]-a[i]))

for i in range(1,len(a)-1):
    print(sm - abs(a[i]-a[i-1]) - abs(a[i+1]-a[i]) + abs(a[i+1]-a[i-1]))
