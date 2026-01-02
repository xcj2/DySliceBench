#全方位木DPによって求める
from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9 + 7)


def get_par_tree(tree: list, par: int) -> list:
    """親を求める"""
    n = len(tree)
    ans = [-1] * n
    visited = [False] * n
    visited[par] = True
    q = deque([par])
    while q:
        pos = q.popleft()
        for next_pos in tree[pos]:
            if visited[next_pos]:
                continue
            visited[next_pos] = True
            ans[next_pos] = pos
            q.append(next_pos)
    return ans


def topological_sort_tree(tree: list, par) -> list:
    n = len(tree)
    ans = [par]
    visited = [False] * n
    visited[par] = True
    q = deque([par])
    while q:
        pos = q.popleft()
        for next_pos in tree[pos]:
            if visited[next_pos]:
                continue
            visited[next_pos] = True
            ans.append(next_pos)
            q.append(next_pos)
    return ans


def dfs1():
    """その頂点の部分木での黒色で塗るパターンを求める"""
    visited = [False] * n
    for pos in tp_list[::-1]:
        visited[pos] = True
        for next_pos in graph[pos]:
            if visited[next_pos]:
                continue
            b1[next_pos] *= (1 + b1[pos])
            b1[next_pos] %= MOD


def dfs2():
    """全方位木DP"""
    for pos in tp_list:
        cnt = 0
        b = 1
        par = par_list[pos]
        for next_pos in graph[pos]:
            if next_pos == par:
                d = child_pos[par][pos]
                tmp_b = ruiseki_child_l[par][d] * ruiseki_child_r[par][-d-2]
                tmp_b %= MOD
                b *= (1 + tmp_b)
                b %= MOD
                child_pos[pos][next_pos] = cnt
                child_val[pos].append(1 + tmp_b)
                cnt += 1
            else:
                b *= (1 + b1[next_pos])
                child_pos[pos][next_pos] = cnt
                child_val[pos].append(1 + b1[next_pos])
                cnt += 1
                b %= MOD
        b2[pos] = b
        ruiseki_child_l[pos] += child_val[pos] 
        ruiseki_child_r[pos] += child_val[pos][::-1]
        for i in range(len(child_val[pos])):
            ruiseki_child_r[pos][i+1] = ruiseki_child_r[pos][i] * ruiseki_child_r[pos][i+1]
            ruiseki_child_l[pos][i+1] = ruiseki_child_l[pos][i] * ruiseki_child_l[pos][i+1]
            ruiseki_child_r[pos][i+1] %= MOD
            ruiseki_child_l[pos][i+1] %= MOD


n, m = map(int, input().split())
MOD = m
info = [list(map(int, input().split())) for i in range(n-1)]
graph = [[] for i in range(n)]
dag = [[] for i in range(n)]

for i in range(n-1):
    a, b = info[i]
    a -= 1
    b -= 1
    graph[b].append(a)
    graph[a].append(b)

par_list = get_par_tree(graph, 0)
tp_list = topological_sort_tree(graph, 0)
b1 = [1] * n
dfs1()

child_pos = defaultdict(lambda :defaultdict(dict))
child_val = [[] for i in range(n)]
ruiseki_child_l = [[1] for i in range(n)]
ruiseki_child_r = [[1] for i in range(n)]
b2 = [0] * n
dfs2()

for num in b2:
    print(num % MOD)
