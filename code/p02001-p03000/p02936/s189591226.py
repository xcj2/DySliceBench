import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,Q=map(int,input().split())
    a=[0]*(N-1)
    b=[0]*(N-1)
    cns=[[] for _ in range(N)]
    for i in range(N-1):
        a[i],b[i]=map(lambda x: int(x)-1,input().split())
        cns[a[i]].append(b[i])
        cns[b[i]].append(a[i])
    l_x=[0]*N
    for i in range(Q):
        p,x=map(int,input().split())
        l_x[p-1]+=x
    c=[0]*N
    c[0]+=l_x[0]
    def saiki(pn,ppn,x):
        for cn in cns[pn]:
            if cn != ppn:
                z=x+l_x[cn]
                c[cn]+=z
                saiki(cn,pn,z)
        return
    saiki(0,0,c[0])
    print(*c)
    

if __name__ == '__main__':
    main()
