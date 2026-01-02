from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def counter():
    cnt = 0
    while True:
        yield cnt
        cnt += 1

def dfs(here, visited, track, count, connect):
    visited |= {here}
    for c in connect[here]:
        if c not in visited:
            dfs(c, visited, track, count, connect)
    track[here] = next(count)

def kosaraju(here, visited, track, count, connect):
    visited |= {here}
    for c in connect[here]:
        if c not in visited:
            kosaraju(c, visited, track, count, connect)
    track[here] = count

vertices, edges = (int(n) for n in input().split(" "))
connect = defaultdict(list)
reversed_connect = defaultdict(list)
for _ in range(edges):
    v1, v2 = (int(n) for n in input().split(" "))
    connect[v1].append(v2)
    reversed_connect[v2].append(v1)

visited = set()
track_gen = counter()
track = [-1 for n in range(vertices)]
for v in range(vertices):
    if v not in visited:
        dfs(v, visited, track, track_gen, connect)

visited = set()
track_gen = counter()
strongly_con = [-1 for n in range(vertices)]
for v in range(vertices - 1 ,- 1, -1):
    here = track.index(v)
    if here not in visited:
        num = next(track_gen)
        kosaraju(here, visited, strongly_con, num, reversed_connect)

q_num = int(input())
for _ in range(q_num):
    v1, v2 = (int(n) for n in input().split(" "))
    if strongly_con[v1] == strongly_con[v2]:
        print(1)
    else:
        print(0)