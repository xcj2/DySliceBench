import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    A, B, N = [int(x) for x in input().split()]

    def f(m):
        return (A * m) // B - A * (m // B)

    l = f(0)
    e = f(N)

    def isOK(mid):
        if f(mid) - l >= 0:
            return True
        else:
            return False
    def isOK2(mid):
        if f(mid) - e >= 0:
            return True
        else:
            return False

    ok = 0
    ng = N + 1

    loopn = 0

    while abs(ok - ng) > 1:
        loopn += 1
        if loopn >= 10 ** 6:
            break
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    ans = max(l, e, f(ok))
    for i in range(max(0, ok - 10000), min(N + 1, ok + 10000)):
        ans = max(ans, f(i))
    for i in range(max(0, ng - 10000), min(N + 1, ng + 10000)):
        ans = max(ans, f(i))

    ok = N
    ng = 0

    loopn = 0

    while abs(ok - ng) > 1:
        loopn += 1
        if loopn >= 10 ** 6:
            break
        mid = (ok + ng) // 2
        if isOK2(mid):
            ok = mid
        else:
            ng = mid

    ans = max(ans, l, e, f(ok))
    for i in range(max(0, ok - 10000), min(N + 1, ok + 10000)):
        ans = max(ans, f(i))
    for i in range(max(0, ng - 10000), min(N + 1, ng + 10000)):
        ans = max(ans, f(i))

    print(max(ans, f(min(B - 1, N))))


if __name__ == '__main__':
    main()
