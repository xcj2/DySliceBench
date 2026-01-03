from math import ceil


# 川の字に分割
def river(x, y):
    diff = ceil(x / 3) - x // 3
    return diff * y


# T字に分割
def t(x, y):
    def f(uy):
        dy = y - uy
        lx = x // 2
        rx = x - lx
        us = x * uy
        ls = lx * dy
        rs = rx * dy
        return max(us, ls, rs) - min(us, ls, rs)

    return min(f(y // 3), f(ceil(y / 3)))


def solve(h, w):
    return min(river(h, w), river(w, h), t(h, w), t(w, h))


def main():
    h, w = map(int, input().split())

    ans = solve(h, w)
    print(ans)


if __name__ == "__main__":
    main()
