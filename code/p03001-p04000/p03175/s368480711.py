import sys
from collections import deque
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


def make_tree_0index(N):
    edge_dic = {}
    for _ in range(N-1):
        x, y = na()
        x -= 1
        y -= 1
        if x in edge_dic:
            edge_dic[x].append(y)
        else:
            edge_dic[x] = [y]
        if y in edge_dic:
            edge_dic[y].append(x)
        else:
            edge_dic[y] = [x]
    return edge_dic


N = ni()
if N == 1:
    print(2)
    exit()
edge_dic = make_tree_0index(N)
ans = [[0] * 2 for _ in range(N)]
mod = 10 ** 9 + 7

parent_array = [-2] * N
parent_array[0] = -1
node1 = deque([0])
node2 = deque([0])

while(len(node1)):
    n = node1.popleft()
    for v in edge_dic[n]:
        if parent_array[v] == -2:
            parent_array[v] = n
            node1.append(v)
            node2.append(v)

while(len(node2)):
    n = node2.pop()
    white = 1
    black = 1
    for v in edge_dic[n]:
        if parent_array[n] == v:
            continue
        white = (white * (ans[v][0] + ans[v][1])) % mod
        black = black * ans[v][0] % mod
    ans[n][0] = white
    ans[n][1] = black


print((ans[0][0] + ans[0][1]) % mod)
