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
ast = input()
bst = input()
cst = input()

ans = 0

for a, b, c in zip(ast,bst,cst):
    if a == b == c:
        continue
    elif a == b or b == c or c == a:
        ans += 1
    else:
        ans += 2
print(ans)