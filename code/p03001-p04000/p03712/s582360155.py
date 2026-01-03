from sys import stderr, setrecursionlimit
from functools import reduce
from operator import add
setrecursionlimit(2147483647)
def getInt():
    return int(input())
def getInts():
    return [int(i) for i in input().split()]
def getIntLines(n=1):
    res = []
    for _ in range(n):
        res.append(getInt())
    return res
def getIntsLines(n=1):
    res = []
    for _ in range(n):
        res.append(getInts())
    return res
def debug(*x, sep=" ", end="\n"):
    for item in x:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)

h, w = getInts()
ans = ['#' *(w+2)]
for _ in range(h):
    line = '#'
    line += input()
    line += '#'
    ans.append(line)
ans.append('#'*(w+2))
print(*ans, sep='\n')