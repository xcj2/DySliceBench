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
dish = []
bsum = 0
for _ in range(n):
    a, b = getInts()
    bsum += b
    dish.append(a+b)
dish.sort(reverse=True)
print(sum(dish[::2]) - bsum)