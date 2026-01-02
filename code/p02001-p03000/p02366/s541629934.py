# GRL_3_A : Articulation Point

import sys

sys.setrecursionlimit(100000)

# input
v, e = map(int, sys.stdin.readline().strip().split())
G = [[] for _ in range(v)]
indeg = [0] * v
for i in range(e):
    s, t = map(int, sys.stdin.readline().strip().split())
    G[s].append(t)
    G[t].append(s)
    indeg[t] += 1

# calc
visit = [False] * v
lowest = [v+1] * v
prenum = [-1] * v
parent = [-1] * v
time = 0


def dfs(current, prev):
    global time
    prenum[current] = time
    lowest[current] = time
    visit[current] = True
    time += 1

    for i in G[current]:
        next = i
        if not visit[next]:
            parent[next] = current

            dfs(next, current)
            lowest[current] = min(lowest[current], lowest[next])
        elif next != prev:
            lowest[current] = min(lowest[current], prenum[next])


def art_points():
    dfs(0, -1)

    np = 0  # root が子を2つ以上持つかカウントする
    articulationPoint = [] # 関節点を保存するリスト
    for i in range(1, v):
        if parent[i] == 0:
            np += 1
        elif lowest[i] >= prenum[parent[i]]:
            if parent[i] not in articulationPoint:
                articulationPoint.append(parent[i])

    if np > 1:
        articulationPoint.append(0)

    # articulationPoint = list(set(articulationPoint))
    articulationPoint.sort()

    return articulationPoint


def main():
    ans = art_points()
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()

