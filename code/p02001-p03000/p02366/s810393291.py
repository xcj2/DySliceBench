from sys import stdin
from collections import deque

def read_graph(n, k):
    A = [ [] for _ in range(n) ]
    for _ in range(k):
        line = stdin.readline().strip().split()
        A[int(line[0])].append(int(line[1]))
        A[int(line[1])].append(int(line[0]))
    return A

def art_points(n, A):
    S = deque([])
    color = ["WHITE"] * n
    time = 0
    prenum = [0] * n
    parent = [0] * n
    lowest = [0] * n
    ap = []

    def dfs(u):
        nonlocal S
        nonlocal color
        nonlocal time
        nonlocal prenum
        nonlocal parent
        nonlocal lowest
        S.appendleft(u)
        color[u] = "GRAY"
        prenum[u] = lowest[u] = time
        parent[u] = -1
        time += 1

        while S:
            try:
                w = S[1]
            except IndexError:
                w = -1
            u = S[0]
            colors = [color[v] for v in A[u]]
            if "WHITE" in colors:
                for v in A[u]:
                    if color[v] == "WHITE":
                        parent[v] = u
                        color[v] = "GRAY"
                        prenum[v] = lowest[v] = time
                        time += 1
                        S.appendleft(v)
                        break
            else:
                for v in A[u]:
                    if color[v] == "GRAY" and v != w:
                        # Backedge(u, v) の prenum[v] と比較
                        lowest[u] = min(lowest[u], prenum[v])
                if parent[u] != -1:
                    # 全ての子ノードのlowestと比較
                    lowest[parent[u]] = min(lowest[u], lowest[parent[u]])
                S.popleft()
                color[u] = "BLACK"
                time += 1

    def obtain_ap():
        np = 0
        for i in range(n):
            p = parent[i]
            if p == 0:
                np += 1
            elif prenum[p] <= lowest[i]:
                if p not in ap:
                    ap.append(p)
        if np > 1:
            ap.append(0)

    dfs(0)
    obtain_ap()

    return ap

n, k = [int(i) for i in input().split()]
A = read_graph(n, k)
ap = art_points(n, A)
for i in sorted(ap):
    if i != -1:
        print(i)

