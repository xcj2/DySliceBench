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

n,l = li()
a = list(li())

exist = False

for i, (ap, an) in enumerate(zip(a[:-1], a[1:])):
    if ap + an >= l:
        bef = [j+1 for j in range(i)]
        aft = [j+1 for j in range(n-2,i,-1)]
        ans = bef + aft + [i+1]
        exist = True
        break

if exist:
    print("Possible")
    for ai in ans:
        print(ai)

else:
    print("Impossible")