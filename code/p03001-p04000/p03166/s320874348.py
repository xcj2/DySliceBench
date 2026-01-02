import sys
sys.setrecursionlimit(10**9)

def dfs(dp,edges,node,visited):
    if node not in visited:
        visited.add(node)
        for kid in edges[node]:
            dfs(dp,edges,kid,visited)
            #print(dp,node,kid)
            dp[node-1] = max(dp[node-1],dp[kid-1])
        if edges[node]:
            dp[node-1] += 1

def solve(edges,n):
    dp = [0]*n
    visited = set()
    for i in range(1,n+1):
        if i not in visited:
            #print(i)
            dfs(dp,edges,i,visited)

    #print(dp)
    print(max(dp))

def main():
    n,m = map(int,input().split())
    edges = {}
    for i in range(1,n+1):
        edges[i] = []

    for i in range(m):
        x,y = map(int,input().split())
        edges[x].append(y)

    solve(edges,n)


main()
