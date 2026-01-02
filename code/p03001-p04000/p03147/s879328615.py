from sys import stderr, setrecursionlimit
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

n = getInt()
h = getInts()
ans = 0
l = 0
r = 0
while l < n:
    r = l
    while l < n and h[l] == 0:
        l += 1
        r += 1
    while r < n and h[r] != 0:
        r += 1
    if r == l:
        break
    tmp = min(h[l:r])
    ans += tmp
    h = h[:l] + list(map(lambda x:x-tmp, h[l:r])) + h[r:]
    debug(l, r, h)

print(ans)
