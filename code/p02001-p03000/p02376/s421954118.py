#import sys
#input = sys.stdin.readline
from collections import defaultdict
INF = 10**9

def dfs_for_Ford_Fulkerson(N,E,capacity,s,g,flowing):
    stack = [(s,INF)]
    root = [0]*N
    root[s] = -1
    V = [False]*N
    V[s] = True
    while stack:
        # print(stack)
        u, flow = stack.pop()
        # print(u, E[u])
        for v in E[u]:
            # print(v)
            # print(V[v])
            # print(v, not V[v], capacity[(u,v)]>0)
            if not V[v] and capacity[(u,v)] > 0:
                root[v] = u
                V[v] = True
                if v == g:
                    if capacity[(u,v)] < flow:
                        flow = capacity[(u,v)]
                    break
                stack.append((v, min(flow, capacity[(u,v)])))
        else:
            continue
        break
    else:
        return False
    ## 更新
    now = g
    while now != s:
        before = root[now]
        capacity[(before, now)] -= flow
        capacity[(now, before)] += flow
        now = before
    flowing[0] += flow
    # print(capacity, flow)
    return True

def Ford_Fulkerson(N,E,capacity, s, g):
    flowing = [0]
    while dfs_for_Ford_Fulkerson(N,E,capacity,s,g, flowing):
        pass
    return flowing[0]

def main():
    N, M = map( int, input().split())
    E = [[] for _ in range(N)]
    capacity = defaultdict( int)
    for i in range(M):
        u, v, c = map( int, input().split())
        E[u].append(v)
        capacity[(u,v)] = c
        E[v].append(u)

    print( Ford_Fulkerson(N,E,capacity,0,N-1))
        
    
if __name__ == '__main__':
    main()

