n, m = map(int, input().split())
import sys
sys.setrecursionlimit(1000000)
c_list = {}
# 辞書の初期化
for node in range(n):
    c_list[node] = []

for _ in range(m):
    a, b = map(int, input().split())
    c_list[a].append(b)
    c_list[b].append(a)

colors = {}


# 色を割り当てていく
def dfs(node, c):
    if node not in colors:
        colors[node] = c
        for next in c_list[node]:
            dfs(next, c)


# stackでも書きたい
# 色の割当が間違っている
def assignColor():
    c = 0
    for node in c_list:
        if node not in colors:
            dfs(node, c)
            c += 1


def checkColor(u, v):
    if colors[u] == colors[v]:
        print('yes')
    else:
        print('no')


assignColor()
k = int(input())
for _ in range(k):
    u, v = map(int, input().split())
    checkColor(u, v)

