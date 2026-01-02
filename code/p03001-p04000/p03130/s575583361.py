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

a1,b1 = getInts()
a2,b2 = getInts()
a3,b3 = getInts()
towns = [a1,a2,a3,b1,b2,b3]
print("YES" if all([towns.count(i) <=2 for i in range(1,5)]) else "NO")