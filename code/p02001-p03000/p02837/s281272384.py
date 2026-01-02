n = int(input())

a = [0] * n
d = [[] for _ in range(n)]
for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        d[i].append(tuple(map(int, input().split())))

def decode(s):
    r = [0] * n
    for i in range(n):
        r[i] = int(bool(s & (1 << i)))
    return r

def validate(s):
    r = decode(s)
    for i in range(n):
        if not r[i]:
            continue
        for x, y in d[i]:
            if r[x - 1] != y:
                return 0
    return sum(r)

def solve():
    ans = 0
    for i in range(2 ** n):
        ans = max(ans, validate(i))
    print(ans)

solve()
