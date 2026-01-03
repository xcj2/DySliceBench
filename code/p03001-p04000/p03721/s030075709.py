from sys import stderr, setrecursionlimit, exit
from collections import defaultdict as dd
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
def debug(*args, sep=" ", end="\n"):
    for item in args:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)

n, k = getInts()
arr = dd(int)
for _ in range(n):
    a, b = getInts()
    arr[a] += b
arr_sorted = sorted(list(arr.items()),key=lambda x:x[0])
i = 0
for key, val in arr_sorted:
    i += val
    if i >= k:
        print(key)
        exit()