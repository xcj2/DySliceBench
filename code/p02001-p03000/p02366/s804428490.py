from typing import List
from typing import Tuple
from sys import setrecursionlimit

setrecursionlimit(100000)

def articulation_points(adj, n):
    low_link = [None for _ in range(n)]
    mark = [False for _ in range(n)]
    id = [-1 for _ in range(n + 1)]
    points = []

    for v in range(n):
        if mark[v]:
            continue
        dfs(v, -1, adj, id, low_link, mark, points)
    points.sort()
    return points

def dfs(v: int, p: int, adj: List[List[int]], id: List[int], low_link: List[int], mark: List[bool], points: List[int]) -> None:
    mark[v] = True
    id[-1] += 1
    id[v] = id[-1]
    low_link[v] = id[v]

    is_articulation_point = False
    childs = 1 if p != -1 else 0 

    for a_v in adj[v]:
        if a_v == p: continue
        if not mark[a_v]:
            childs += 1
            dfs(a_v, v, adj, id, low_link, mark, points)
            low_link[v] = min(low_link[v], low_link[a_v])
            if childs > 1 and id[v] <= low_link[a_v]:
                is_articulation_point = True
        else:
            low_link[v] = min(low_link[v], id[a_v])
    if is_articulation_point:
        points.append(v)

def read() -> Tuple[List[List[int]], int]:
    v, e = tuple([int(i) for i in input().split()])

    adj = [[] for _ in range(v)]

    for i in range(e):
        v1, v2 = tuple([int(j) for j in input().split()])
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    return adj, v

def write(point_list):
    for point in point_list:
        print(point)

adj, n = read()
articulation_point_list = articulation_points(adj, n)
write(articulation_point_list)

