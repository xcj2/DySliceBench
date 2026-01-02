import sys


def val(l, r, d, Vs):
    jewels = Vs[:l] + list(reversed(Vs))[:r]
    return sum(sorted(jewels)[d:])

def cond(l, r, d, k, N):
    return l + r >= 0 and l + r <= min([k, N]) and d <= l + r


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    Vs = list(map(int, input().split()))

    ans = 0
    for k in range(K+1):
        for l in range(min([k+1, N+1])):
            for r in range(min([k+1, N+1])):
                d = k - l - r
                if cond(l, r, d, k, N):
                    ans = max(ans, val(l, r, d, Vs))
    print(ans)


if __name__ == '__main__':
    main()
