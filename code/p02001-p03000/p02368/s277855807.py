from sys import setrecursionlimit
from collections import deque

setrecursionlimit(20001)

def read():
    v, e = tuple([int(e) for e in input().split()])
    adj = [[] for _ in range(v)]
    for _ in range(e):
        v_from, v_to = tuple([int(e) for e in input().split()])
        adj[v_from].append(v_to)

    return adj, v


def find_strong_components(adj, n):
    id = [0 for _ in range(n + 1)]
    low_link = [0 for _ in range(n)]
    mark = [False for _ in range(n)]
    in_stack = [False for _ in range(n)]
    st = deque()
    
    for v in range(n):
        if mark[v]: continue
        dfs(v, mark, id, low_link, adj, in_stack, st)
    return low_link

def dfs(v, mark, id, low_link, adj, in_stack, st):
    mark[v] = True
    in_stack[v] = True
    low_link[v] = id[v] = id[-1]
    id[-1]+=1

    st.append(v)
    for n_v in adj[v]:
        if not mark[n_v]:
            dfs(n_v, mark, id, low_link, adj, in_stack, st)
        if in_stack[n_v]:
            low_link[v] = min(low_link[v], low_link[n_v])

    if id[v] == low_link[v]:
        while st:
            top_v = st.pop() 
            low_link[top_v] = id[v]
            in_stack[top_v] = False
            if top_v == v:
                break

def write(low_link):
    q = int(input())
    for _ in range(q):
        v1, v2 = tuple([int(e) for e in input().split()])
        if low_link[v1] == low_link[v2]:
            print('1')
        else:
            print('0')

adj, n = read()
low_link = find_strong_components(adj, n)
write(low_link)
