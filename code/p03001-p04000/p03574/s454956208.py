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

h, w = getInts()
grid = [['.' for _ in range(w+2)]]
for _ in range(h):
    tmp = ['.']
    tmp.extend(list(input()))
    tmp.append('.')
    grid.append(tmp)
grid.append(['.' for _ in range(w+2)])

for i in range(1,h+1):
    for j in range(1,w+1):
        if grid[i][j] == '#':
            continue
        count = 0
        for k in range(-1,2):
            for l in range(-1,2):
                if grid[i+k][j+l] == '#':
                    count += 1
        grid[i][j] = count
for l in grid[1:-1]:
    print(*l[1:-1], sep='')
