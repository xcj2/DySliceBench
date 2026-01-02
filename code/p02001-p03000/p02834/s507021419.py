def main():
    import sys
    input=sys.stdin.readline
    sys.setrecursionlimit(100000000)

    n,u,v=map(int,input().split())
    u-=1
    v-=1
    tree=[[] for i in range(n)]
    for i in range(n-1):
        a,b=map(int,input().split())
        a-=1
        b-=1
        tree[a].append(b)
        tree[b].append(a)
    
    depth_u=[0]*n #uからの距離
    depth_v=[0]*n #vからの距離
    
    def dfs1(i,before=-1):
        for e in tree[i]:
            if e!=before:
                depth_u[e]=depth_u[i]+1
                dfs1(e,i)
    
    def dfs2(i,before=-1):
        for e in tree[i]:
            if e!=before:
                depth_v[e]=depth_v[i]+1
                dfs2(e,i)
    
    dfs1(u)
    dfs2(v)

    ans=depth_v[u]-1
    for i in range(n):
        if len(tree[i])==1 and depth_u[i]<depth_v[i]:
                ans=max(ans,depth_v[i]-1)
    print(ans)

if __name__=='__main__':
    main()