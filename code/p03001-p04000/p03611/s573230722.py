from sys import stdin, stderr, setrecursionlimit, exit
from collections import Counter
setrecursionlimit(2147483647)
def getint():
    return int(stdin.readline().rstrip('\r\n'))
def getints():
    return [int(i) for i in stdin.readline().rstrip('\r\n').split()]
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
c = Counter()

for i in a:
    c[i-1] += 1
    c[i] += 1
    c[i+1] += 1

print(c.most_common(1)[0][1])
