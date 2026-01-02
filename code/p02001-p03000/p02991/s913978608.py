import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

def main():
    N,M = list(map(int,input().split()))

    e_list = [[] for i in range(3*N)]

    def z(i,j):
        return i + j*N

    for i in range(M):
        u,v = list(map(int,input().split()))
        u,v = u-1,v-1
        e_list[z(u,0)].append(z(v,1)) 
        e_list[z(u,1)].append(z(v,2)) 
        e_list[z(u,2)].append(z(v,0))

    S,T = list(map(int,input().split()))
    S,T = S-1,T-1
    from collections import deque

    vi = z(S,0)  #change
    INF = float('inf')

    Q = deque([vi])

    checked_list = [False]*3*N
    checked_list[vi]=True

    min_path_list = [INF]*3*N #change
    min_path_list[vi] = 0

    while len(Q)>0:
        v = Q.pop()
        for v1 in e_list[v]:
            if not checked_list[v1]:
                checked_list[v1]=True
                Q.appendleft(v1)
                min_path_list[v1]=min(min_path_list[v1],min_path_list[v]+1) #change

    if min_path_list[z(T,0)]<10**9:
        print(min_path_list[z(T,0)]//3)
    else:
        print(-1)

if __name__ == '__main__':
    main()

