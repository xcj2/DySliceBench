import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    def dfs(start):
        stack=[start]
        used=[False]*N
        d=[-1]*N
        d[start]=0
        while stack:
            node=stack.pop()
            used[node]=True
            for x in cns[node]:
                if not used[x]:
                    d[x]=d[node]+1
                    stack.append(x)
        return d
    
    N,u,v=map(int,input().split())
    u-=1
    v-=1
    A,B=[0]*(N-1),[0]*(N-1)
    cns=[[] for _ in range(N)]
    for i in range(N-1):
        A[i],B[i]=map(lambda x: int(x)-1,input().split())
        cns[A[i]].append(B[i])
        cns[B[i]].append(A[i])

    u_l = dfs(u)
    v_l = dfs(v)
    ans=0
    for U,V in zip(u_l,v_l):
        if V > U:
            ans=max(ans,V-1)
    print(ans)

if __name__ == '__main__':
    main()
