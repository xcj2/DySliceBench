import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    inf=10**9
    n,*abc=MI()
    abc.sort()
    a,b,c=abc
    dp={(0,0,0):0}
    for _ in range(n):
        l=II()
        ndp={}
        for xyz,s in dp.items():
            ndp.setdefault(xyz,inf)
            ndp[xyz]=min(ndp[xyz],s)
            for i in range(3):
                nx=list(xyz)
                ns=s+10 if nx[i] else s
                nx[i]+=l
                t=tuple(sorted(nx))
                ndp.setdefault(t,inf)
                ndp[t]=min(ndp[t],ns)
            dp=ndp

    ans=inf
    for (x,y,z),s in dp.items():
        if x*y*z==0:continue
        cur=abs(x-a)+abs(y-b)+abs(z-c)+s
        ans=min(ans,cur)

    print(ans)

main()