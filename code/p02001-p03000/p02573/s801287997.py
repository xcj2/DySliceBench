import bisect
import sys
import math
input = sys.stdin.readline
import functools

from collections import defaultdict

############ ---- Input Functions ---- ############

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- Solution ---- ############

def dfs(i, edges, visited):
    s = []
    if not visited[i]:
        s.append(i)
        visited[i] = True
    res = 0
    while len(s) > 0:
        v = s.pop()
        res += 1
        for i in edges[v]:
            if not visited[i]:
                s.append(i)
                visited[i] = True

    return res

def solve():
    [N, M] = inlt()
    edges = defaultdict(set)
    visited = [False for i in range(N)]

    for i in range(M):
        [a, b] = inlt()
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)

    res = 0
    for i in range(N):
        res = max(res, dfs(i, edges, visited))
    
    return res

    

if len(sys.argv) > 1 and sys.argv[1].startswith("input"):
    f = open("./" + sys.argv[1], 'r')
    input = f.readline

res = solve()
print(str(res))
