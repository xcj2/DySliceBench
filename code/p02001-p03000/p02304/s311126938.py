import bisect


def memoize(f):
    cache = {}

    def func(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return func


@memoize
def get_bisect(y):
    return bisect.bisect(vy, (y,))


n = int(input())
vx, vy = [], []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        vx.append((x1, y1, y2))
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        vy.append((y1, x1, x2))
vy.sort()

ans = 0

for x, y1, y2 in vx:
    it1, it2 = get_bisect(y1), get_bisect(y2 + 1)
    ans += sum(1 for y, x1, x2 in vy[it1:it2] if x1 <= x <= x2)

print(ans)