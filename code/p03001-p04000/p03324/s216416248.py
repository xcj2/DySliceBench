def main():
    D, N = map(int, input().split())

    ans = f(D, N)
    print(ans)


def WA(D, N):
    D, N = map(int, input().split())

    if D == 0:
        ans = N
        if N == 100:
            ans = 101
    elif D == 1:
        xs = range(100, 100 * 101, 100)
        ans = xs[N-1]
    else:
        # D=2
        xs = range(100**2, (100 ** 2) * 101, 100**2)
        ans = xs[N-1]

    print(ans)


def f(D, N):
    xs = range(100**D, (100 ** D) * 102, 100**D)
    ans = xs[N-1]
    a = ans // (100**D)
    if a >= 100 and a % 100 == 0:
        ans = xs[N]

    return ans


if __name__ == '__main__':
    main()
