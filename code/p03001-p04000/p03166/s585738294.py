import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N,M=map(int,input().split())
    edge=[[] for _ in range(N)]
    s=set(range(N))
    for _ in range(M):
        x,y=map(lambda x: int(x)-1,input().split())
        edge[x].append(y)
        try:
            s.remove(y)
        except:
            pass
    que=list(s)
    memo=[0]*N
    def saiki(v):
        if memo[v]:
            return memo[v]
        tmp=0
        for nv in edge[v]:
            memo[v]=max(memo[v],saiki(nv)+1)
            tmp=max(tmp,memo[v])
        return tmp
    ans=0
    for v in que:
        ans=max(ans,saiki(v))
    print(ans)
    
    

if __name__ == '__main__':
    main()
