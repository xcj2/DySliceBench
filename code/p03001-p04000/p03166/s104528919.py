import sys
from collections import deque
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


def cal(e):
    if ans_array[e] != -1:
        return ans_array[e]
    ans = 0
    if e in node_dic:
        for x in node_dic[e]:
            ans = max(ans, cal(x) + 1)
    ans_array[e] = ans
    return ans


N, M = na()
node_dic = {}
no_in = [1] * N

for _ in range(M):
    x, y = na()
    if x-1 in node_dic:
        node_dic[x-1].append(y-1)
    else:
        node_dic[x-1] = [y-1]
    no_in[y-1] = 0


# print(node_dic, no_in)


ans_array = [-1] * N

edge = deque([])

for i, x in enumerate(no_in):
    if x == 1:
        cal(i)


print(max(ans_array))
