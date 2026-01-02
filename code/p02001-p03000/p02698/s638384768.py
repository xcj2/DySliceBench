import sys
input = sys.stdin.buffer.readline
import bisect
import copy
from collections import deque
sys.setrecursionlimit(10**7)

def main():
    N = int(input())
    a = list(map(int,input().split()))
    INF = 10**12
    
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v = map(int,input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
        
    def LIS(dp,num):
        ind = bisect.bisect_left(dp,num)
        ret = dp[ind]
        dp[ind] = num
        return ind,ret
    
    dp = [INF]*(N+2)
    dp[0] = -INF

    ans = [0]*N
    q = deque([])
    
    def DFS(prev,now,dp):
        while q:
            s,t,ind,num = q.pop()
            if t == prev:
                q.append((s,t,ind,num))
                break
            else:
                dp[ind] = num
        ind,num = LIS(dp,a[now])
        ans[now] = max(ind,ans[prev])
        q.append((prev,now,ind,num))
        for fol in edge[now]:
            if fol != prev:
                DFS(now,fol,dp)

    DFS(-1,0,dp)
    print(*ans,sep="\n")
 
if __name__ == "__main__":
    main()
