#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 091
# C - 2D Plane 2N Points

from sys import stdin

def graph(red, blue):
    """
    Return the adjacent list of the bipartite graph that consists of
    the red vertices and the blue vertices.
    The red vertices are numbered as 0, 1, ..., N - 1 and
    the blue vertices are numbered as N, N + 1, ..., 2N - 1.
    The returned list contains 2N elements, each of which is
    the adjacent list of a vertex.
    """
    N = len(red)
    adj = [[] for i in range(2 * N)]
    for i in range(N):
        a, b = red[i]
        for j in range(N):
            c, d = blue[j]
            if a < c and b < d:
                adj[i]    .append(j + N)
                adj[j + N].append(i)
    return adj

def dfs(v, g, M, visited, path):
    if visited[v]: return None
    visited[v] = True
    for u in g[v]:
        w = M[u]
        if w == None: return path + [v, u]
        apath = dfs(w, g, M, visited, path + [v, u])
        if apath != None: return apath
    return None

def augPath(g, M):
    """
    For a graph g and a current matching M,
    return an augmenting path.
    If g does not have an augmenting path, then return None.
    """
    nvertices = len(g)
    for v in range(nvertices):
        if M[v] == None:
            visited = [False for v in range(nvertices)]
            apath = dfs(v, g, M, visited, [])
            if apath != None: return apath
    return None

def solve(red, blue):
    g = graph(red, blue)
    nvertices = len(g)
    # empty matching
    M = [None for v in range(nvertices)]
    # Find the maximum matching.
    while True:
        apath = augPath(g, M)
        if apath == None: break
        # Alter the matching.
        for i in range(0, len(apath), 2):
            v, u = apath[i : i + 2]
            M[v], M[u] = u, v
    nmatching = sum(1 for m in M if m != None) // 2
    return nmatching

def readIntPairList(N):
    """Read a list of N pairs of ints from stdin."""
    ls = []
    for i in range(N):
        a, b = [int(w) for w in stdin.readline().split()]
        ls.append((a, b))
    return ls

N = int(stdin.readline())
red  = readIntPairList(N)
blue = readIntPairList(N)
print(solve(red, blue))
