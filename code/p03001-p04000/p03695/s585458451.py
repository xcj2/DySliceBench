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
a = getInts()
colors = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for rate in a:
    if rate <= 399:
        colors[0] += 1
    elif rate <= 799:
        colors[1] += 1
    elif rate <= 1199:
        colors[2] += 1
    elif rate <= 1599:
        colors[3] += 1
    elif rate <= 1999:
        colors[4] += 1
    elif rate <= 2399:
        colors[5] += 1
    elif rate <= 2799:
        colors[6] += 1
    elif rate <= 3199:
        colors[7] += 1
    else:
        colors[8] += 1

monocolors = len(list(filter(lambda x:x!=0,colors[:-1])))
if monocolors == 0:
    print(1, colors[8])
else:
    print(monocolors, monocolors + colors[8])