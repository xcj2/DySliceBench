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

n,a,b = li()
s = ns()

cnt = 0
frank = 1

for i, si in enumerate(s):
    if si == 'a':
        if cnt < a+b:
            cnt += 1
            print("Yes")
        else:
            print("No")
            
    elif si == 'b':
        if cnt < a+b and frank <= b:
            cnt += 1
            frank += 1
            print("Yes")
        else:
            print("No")
            
    else:
        print("No")