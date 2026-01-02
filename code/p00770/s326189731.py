import sys
from collections import defaultdict

N = 10**6 + 1
p = list(range(N))
p[1] = 0
for i in range(2, int(N**.5) + 1):
    p[i * 2::i] = [0] * len(p[i * 2::i])

cart2num = {}


def cart2spi(x, y):
    size = max(abs(x), abs(y))
    if x + y > 0:
        num = (2 * size - 1) ** 2
        sx, sy = size, 1 - size
        num += y - sy + sx - x
    else:
        num = (2 * size) ** 2
        sx, sy = -size, size
        num += sy - y + x - sx
    return num


def spi2cart(n):
    root = int(n ** .5)
    diff = n - root ** 2
    if root % 2:
        x, y = root // 2 + 1, -root // 2 + 1
        dx, dy = -1, 1
    else:
        x, y = -root // 2, root // 2
        dx, dy = 1, -1
    x += dx * max(diff - root, 0)
    y += dy * min(diff, root)
    return x, y


def solve(max_p, s):
    prv = {spi2cart(s - 1): [1, s] if p[s] else [0, 0]}
    res = []
    while 1:
        nxt = defaultdict(lambda: [0, 0])
        for x, y in prv:
            ny = y - 1
            for dx in [-1, 0, 1]:
                nx = x + dx
                if (nx, ny) in cart2num:
                    num = cart2num[nx, ny]
                else:
                    num = cart2num[nx, ny] = cart2spi(nx, ny) + 1
                if num > max_p:
                    if dx == 0:
                        res.append(prv[x, y])
                    continue
                nxt_cnt, prv_cnt = nxt[nx, ny][0], prv[x, y][0]
                if p[num]:
                    if nxt_cnt < prv_cnt + 1:
                        nxt[nx, ny] = [prv_cnt + 1, num]
                    elif nxt_cnt == prv_cnt + 1:
                        nxt[nx, ny][1] = max(nxt[nx, ny][1], num)
                else:
                    if nxt_cnt < prv_cnt:
                        nxt[nx, ny] = prv[x, y]
                    elif nxt_cnt == prv_cnt:
                        nxt[nx, ny][1] = max(nxt[nx, ny][1], prv[x, y][1])
        if not nxt:
            break
        prv = nxt
    return max(res)


for e in sys.stdin.readlines()[:-1]:
    m, n = map(int, e.split())
    print(*solve(m, n))
