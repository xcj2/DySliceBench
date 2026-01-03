from sys import stderr, setrecursionlimit
from functools import reduce
from operator import add
from collections import defaultdict as dd
setrecursionlimit(2147483647)
def f(): return [int(i) for i in input().split()]
def yes(n): print("Yes" if n else "No")
def debug(*x, sep=" ", end="\n"):
    for item in x:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)

n, m = f()
graph = dd(list)
for i in range(m):
    a, b = f()
    graph[a].append(b)

for a in graph[1]:
    if n not in graph[a]:
        continue
    print("POSSIBLE")
    break
else:
    print("IMPOSSIBLE")