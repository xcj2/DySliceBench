def binaryUpper(n, a):
    ok = -1
    ng = len(a)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # print("n:", n, "idx:", mid, "val:", a[mid], ok, ng, file=sys.stderr)
        if a[mid] <= n:
            ok = mid
        else:
            ng = mid
    return ng


def binaryLower(n, a):
    ok = len(a)
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # print("n:", n, "idx:", mid, "val:", a[mid], ok, ng, file=sys.stderr)
        if a[mid] >= n:
            ok = mid
        else:
            ng = mid
    return ok


def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(binaryLower(k, a), binaryUpper(k, a))


resolve()

