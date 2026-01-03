from sys import stderr, setrecursionlimit
setrecursionlimit(2147483647)
def getint():
    return int(input())
def getints():
    return [int(i) for i in input().split()]
def getintlines(n=1):
    res = []
    for _ in range(n):
        res.append(getint())
    return res
def getintslines(n=1):
    res = []
    for _ in range(n):
        res.append(getints())
    return res
def debug(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

n = getint()
a = getints()

twice = list(filter(lambda x:x%4==2, a))
quad = list(filter(lambda x:x%4==0, a))

if len(quad) >= n//2:
    print("Yes")
elif len(twice) + 2*len(quad) >= n:
    print("Yes")
else:
    print("No")