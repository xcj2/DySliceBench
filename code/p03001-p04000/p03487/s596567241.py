from sys import stderr, setrecursionlimit
from collections import Counter
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
a = Counter(getints())
debug(a)
ans = 0

for k, v in a.items():
    if v - k >= 0:
        ans += v - k
    else:
        ans += v
    
print(ans)

