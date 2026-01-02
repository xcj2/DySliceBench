import sys


def _s(): return sys.stdin.readline().strip()


def _ia(): return map(int, sys.stdin.readline().strip().split())


def walk(s, w1, h1, x, y, cur, v1, v2):
    if s[y][x] is not None:
        return
    s[y][x] = cur
    v1.add((x, y))
    for hi in range(max(0, y - 2), min(h1, y + 2) + 1):
        for wi in range(max(0, x - 2), min(w1, x + 2) + 1):
            if s[hi][wi] is None:
                v2.add((wi, hi))

    if x > 0:
        walk(s, w1, h1, x-1, y, cur, v1, v2)
    if x < w1:
        walk(s, w1, h1, x+1, y, cur, v1, v2)
    if y > 0:
        walk(s, w1, h1, x, y-1, cur, v1, v2)
    if y < h1:
        walk(s, w1, h1, x, y+1, cur, v1, v2)


def main():
    h, w = _ia()
    sh, sw = map(lambda x: x-1, _ia())
    gh, gw = map(lambda x: x-1, _ia())
    s = [[0]*w for _ in range(h)]
    for hi in range(h):
        for wi, c in enumerate(_s()):
            if c == '.':
                s[hi][wi] = None
            else:
                s[hi][wi] = -1

    p = [(sw, sh)]
    c = 0
    h1, w1 = h-1, w-1
    while len(p) > 0:
        v1 = set()
        v2 = set()
        for pi in p:
            walk(s, w1, h1, *pi, c, v1, v2)
        p = v2 - v1
        c += 1
    ans = s[gh][gw]
    return ans if ans is not None else -1


if __name__ == "__main__":
    print(main())
