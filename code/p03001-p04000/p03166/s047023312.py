import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
def rec(v):
    if dp[v]!=-1:return dp[v]
    res=0
    for nv in graph[v]:
        res=max(res,rec(nv)+1)
    dp[v]=res
    return res
def main():
    n,m=map(int,input().split())
    XY=[tuple(map(int,input().split())) for i in range(m)]
    global dp,graph
    graph=[[]for _ in range(n)]
    for x,y in XY:
        graph[x-1].append(y-1)
    dp=[-1]*n #頂点i(0-)を始点としたときの有効パスの長さの最大値
    ans=0
    for v in range(n):
        ans=max(ans,rec(v))
    print(ans)

if __name__=='__main__':
    main()