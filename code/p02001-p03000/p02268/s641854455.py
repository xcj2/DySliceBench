def is_included(i, n):
    return True if S[i] >= n else False


def search(n):
    inc = N
    exc = -1
    while abs(inc-exc) > 1:
        mid = (exc+inc) // 2
        if is_included(mid, n):
            inc = mid
        else:
            exc = mid
    return inc < N and S[inc] == n


def main():
    ans = 0
    for t in T:
        if search(t):
            ans += 1
    print(ans)


if __name__ == "__main__":
    N = int(input())
    S = sorted([int(s) for s in input().split()])
    Q = int(input())
    T = [int(t) for t in input().split()]
    main()
