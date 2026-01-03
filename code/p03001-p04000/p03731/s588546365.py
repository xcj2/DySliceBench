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
def debug(*args, sep=" ", end="\n"):
    for item in args:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)

n, t = getInts()
tl = getInts()
ans = 0
last = 0
last_head = 0
for v in tl:
    if v <= last:
        last += (v + t) - last
    else:
        ans += last - last_head
        last_head = v
        last = last_head + t
ans += last - last_head
print(ans)