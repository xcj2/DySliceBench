import sys
input=sys.stdin.readline
def main():
    n=int(input())
    Edges=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1
        Edges[a].append(b)
        Edges[b].append(a)
    m=int(input())
    C=[]
    for _ in range(m):
        u,v=map(int,input().split())
        u-=1; v-=1
        C.append((u,v))
    
    def normalized(u,v):
        return (min(u,v),max(u,v))
    def findpath(u,v,visited=None):
        if visited is None:
            visited=set()
        if u==v:
            return set()
        if u in visited:
            return None
        visited.add(u)
        for x in Edges[u]:
            P=findpath(x,v,visited)
            if P is not None:
                P.add(normalized(u,x))
                return P
    def set_path(Pairs,Paths):
        if len(Pairs)<=1:
            yield ((Pairs[0],),Paths[Pairs[0]])
            yield ((),set())
        else:
            for S,P in set_path(Pairs[1:],Paths):
                yield ((Pairs[0],)+S,P|Paths[Pairs[0]])
                yield (S,P)
    
    Paths={}
    for u,v in C:
        Paths[(u,v)]=findpath(u,v)
    ans=pow(2,(n-1))
    for S,P in set_path(C,Paths):
        l=len(S)
        if l<=0:
            continue
        c=pow(2,(n-1)-len(P))
        flag=1 if l%2==0 else -1
        ans+=flag*c
    print(ans)
    
if __name__=='__main__':
    main()