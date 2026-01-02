def main():
    from functools import lru_cache
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
    
    depth=[0]*n
    depth[v]=0
    def dfs(i,before=-1):
        for e in tree[i]:
            if e!=before:
                depth[e]=depth[i]+1
                dfs(e,i)
    dfs(v)
    #print(depth)
    
    max_depth=[-1]*n
    max_depth[v]=0   
    @lru_cache(maxsize=None)
    def dfs2(i,before=-1):
        t=-1
        for e in tree[i]:
            if e!=before:
                t=max(t,dfs2(e,i))
        if t!=-1:
            max_depth[i]=t
            return max_depth[i]
        else:
            max_depth[i]=depth[i]
            return max_depth[i]
            
    dfs2(v)   
    #print(max_depth)
    
    lim=depth[u]
    i,key=u,u
    while i!=v:
        if 2*depth[i]>lim and max_depth[key] < max_depth[i]:
            key=i
            
        for e in tree[i]:
            if depth[e]<depth[i]:
                i=e
                break
                
    print(max_depth[key]-1) 
if __name__=='__main__':
    main()

