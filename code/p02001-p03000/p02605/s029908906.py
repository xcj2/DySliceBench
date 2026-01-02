import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


inf=10**16
n=II()
xyu=[SI().split() for _ in range(n)]
dir="LRDU"
xyu=[(int(x),int(y),dir.index(u)) for x,y,u in xyu]
xyu.sort()

ans=inf
# 左向き
ytox=defaultdict(int)
hu=defaultdict(list)
sei=defaultdict(list)
for x,y,u in xyu:
    if u==1:
        ytox[y]=x
    if u==2:hu[x+y]=[x,y]
    if u==3:sei[x-y]=[x,y]
    if u==0:
        if y in ytox:
            ans=min(ans,(x-ytox[y])*5)
        if x+y in hu:
            ans=min(ans,abs(x-hu[x+y][0])*10)
        if x-y in sei:
            ans=min(ans,abs(x-sei[x-y][0])*10)

# 右
hu=defaultdict(list)
sei=defaultdict(list)
for x,y,u in xyu[::-1]:
    if u==3:hu[x+y]=[x,y]
    if u==2:sei[x-y]=[x,y]
    if u==1:
        if x+y in hu:
            ans=min(ans,abs(x-hu[x+y][0])*10)
        if x-y in sei:
            ans=min(ans,abs(x-sei[x-y][0])*10)

xyu.sort(key=lambda x:x[1])
ytox=defaultdict(int)
hu=defaultdict(list)
sei=defaultdict(list)
for x,y,u in xyu:
    if u==3:
        ytox[x]=y
    if u==2:
        if x in ytox:
            ans=min(ans,(y-ytox[x])*5)

if ans==inf:print("SAFE")
else:print(ans)
