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

n,q = get_nums_l()

lines = sys.stdin.readlines()
edges = list(map(lambda s:list(map(int, s.split(" "))), lines[:n-1]))
queries = list(map(lambda s:list(map(int, s.split(" "))), lines[n-1:]))

scores = [0] * (n+1)

for q in queries:
    scores[q[0]] += q[1]

queue = deque()
mark = [False] * (n+1)
mark[1] = True


childrens = [ [] for _ in range(n+1) ]
for e in edges:
    a = e[0]
    b = e[1]
    childrens[a].append(b)
    childrens[b].append(a)


queue.append(1)

while queue:
    a = queue.popleft()
    children = childrens[a]
    for b in children:
        if not mark[b]:
            scores[b] += scores[a]
            mark[b] = True
            queue.append(b)

print(" ".join(map(str,scores[1:])))
