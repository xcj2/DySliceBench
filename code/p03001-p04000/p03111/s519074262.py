from itertools import product
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
    inf=10**16
    n,*abc=MI()
    ll=[II() for _ in range(n)]

    ans=inf
    for pp in product(range(4),repeat=n):
        ss=[0]*3
        cnt=[0]*3
        for l,p in zip(ll,pp):
            if p==3:continue
            ss[p]+=l
            cnt[p]+=1
        cur=0
        for i in range(3):
            if cnt[i]==0:
                cur=inf
                break
            cur+=(cnt[i]-1)*10+abs(abc[i]-ss[i])
        #print(pp,cur)
        ans=min(ans,cur)

    print(ans)

main()