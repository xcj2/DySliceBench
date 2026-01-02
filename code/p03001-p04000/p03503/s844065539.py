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
f = getintslines(n)
p = getintslines(n)

# すべての営業パターンについて、全探索(1024通りなので全体で10^5オーダーであり間に合う)
# |profit| <= NP_{i,j}なので絶対値はたかだか10^9
profit = -10**10

for sale in range(1,1025):
    shops = [0]*n
    pattern = format(sale, '010b')
    for i, time in enumerate(pattern):
        if time == '1':
            for j in range(n):
                shops[j] += f[j][i]
    tmp = 0
    for i, s in enumerate(shops):
        tmp += p[i][s]
    profit = max(tmp, profit)
    
print(profit)
