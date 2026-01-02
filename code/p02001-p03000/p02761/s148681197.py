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
    def ng():
        print(-1)
        exit()

    n,m=MI()
    ans=[-1]*n
    for _ in range(m):
        s,c=MI()
        s-=1
        if ans[s]==-1 or ans[s]==c:ans[s]=c
        else:ng()
    if n>1 and ans[0]==0:ng()
    for i in range(n):
        if ans[i]==-1:
            if i==0 and n>1:ans[i]=1
            else:ans[i]=0
    print(*ans,sep="")

main()