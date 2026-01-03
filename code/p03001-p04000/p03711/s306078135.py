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

x, y = getInts()
g1 = [1,3,5,7,8,10,12]
g2 = [4,6,9,11]
print("Yes" if (x in g1 and y in g1) or (x in g2 and y in g2) or (x == y == 2) else "No")