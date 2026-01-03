import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

def log(*args):
    print(*args, file=sys.stderr)


n = int(input())
lines = sys.stdin.readlines()
edges = [ [] for _ in range(n+1) ]
for i in range(n-1):
    e = tuple(map(int, lines[i].split(" ")))
    log(e)
    edges[e[0]].append((e[1],e[2]))
    edges[e[1]].append((e[0],e[2]))

q,k = map(int, lines[n-1].split(" "))

ddd = [0] * (n+1)


que = deque()
que.append(k)
def bfs(x):
    for y, d in edges[x]:
        if ddd[y]:
            continue
        ddd[y] = ddd[x] + d
        que.append(y)


while que:
    bfs(que.pop())

for i in range(n, n+q):
    x, y = map(int, lines[i].split(" "))
    log(x,y)
    print(ddd[x] + ddd[y])
