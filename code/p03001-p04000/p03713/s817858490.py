import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def core(h, H, W):
    if W % 2 == 0:
        return abs(h * W - (H - h) * (W // 2))
    else:
        a, b, c = h * W, (H - h) * (W // 2), (H - h) * (W // 2 + 1)
        return max(abs(a - b), abs(b - c), abs(c - a))


def solve(H, W):
    ans = abs((H // 3) * W - ((H + 2) // 3) * W)

    if H % 3 == 0:
        ans = min(ans, core(H // 3, H, W))
    else:
        ans = min(ans, core(H // 3, H, W), core(H // 3 + 1, H, W))

    return ans


def main():
    H, W = map(int, readline().split())

    ans = min(solve(H, W), solve(W, H))

    print(ans)
    return


if __name__ == '__main__':
    main()
