from collections import deque
import math
from functools import reduce

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n = int(input())
ans = [-1] * n
ans[0] = 0

edges = [ [] for _ in range(n)]
for i in range(n-1):
    u,v,w = get_nums_l()
    edges[u-1].append([v-1,w%2==0])
    edges[v-1].append([u-1,w%2==0])

def aaa(x):
    # xを含むエッジ

    # breakpoint()

    for edge in edges[x]:
        to = edge[0] # edgeのうちxじゃないほう
        if ans[to] != -1:
            continue
        same = edge[1]
        ans[to] = ans[x] ^ (not same)

        queue.append(to)

queue = deque()
queue.append(0)
while queue:
    aaa(queue.popleft())
for annn in ans:
    print(annn)