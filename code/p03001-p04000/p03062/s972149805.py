import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

n=getint()
a=getints()
inf = 1 << 60

cache=[[-inf] * 2 for _ in range(n)]

def solve(pos, minus):
    if pos == n - 1:
        return -a[pos] if minus else a[pos]
    res = cache[pos][minus]
    if res > -inf:
        return res
    now = a[pos] if minus == 0 else -a[pos]
    res1 =  now + solve(pos + 1, 0)
    res2 = -now + solve(pos + 1, 1)
    res  = max(res1, res2)
    cache[pos][minus] = res
    return res

for i in range(n-1,-1,-1):
    solve(i, 0)
    solve(i, 1)

res = solve(0, 0)
print(res)