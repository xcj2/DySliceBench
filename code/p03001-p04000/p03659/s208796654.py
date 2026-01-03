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
snuke = sum(a[:-1])
arai = a[-1]
ans = abs(snuke-arai)
for i in range(2, n):
    debug(a[-i])
    snuke -= a[-i]
    arai += a[-i]
    ans = min(abs(snuke - arai), ans)
    
print(ans)
