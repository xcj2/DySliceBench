from sys import stderr, setrecursionlimit, exit
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
def debug(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

n, m = getInts()
x = sorted(getInts())

if n >= m:
    print(0)
    exit()

b = sorted([x[i+1] - x[i] for i in range(m-1)])

print(sum(b[:m-n]))
