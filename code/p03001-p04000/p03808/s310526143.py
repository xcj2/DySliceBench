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
a = list(li())

exist = True

# aの合計は1~nの和の倍数
if sum(a) % (n*(n+1)//2) != 0:
    exist = False

if exist:
    # 操作の回数
    com = sum(a) // (n*(n+1)//2)
    
    # となりとの差
    diff = [a[i] - a[i-1] for i in range(n)]
    ed = []
    for diffi in diff:
        if (com-diffi) % n != 0:
            exist = False
            break
        else:
            ed.append((com-diffi) // n)
    
    if exist:
        if sum(ed) != com or any([edi < 0 for edi in ed]):
            exist = False
        
if exist:
    print("YES")
else:
    print("NO")