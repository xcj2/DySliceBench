# ABC144E - Gluttony
def binary_search(upper_bound: int = 1 << 60, lower_bound: int = -1) -> int:
    ok, ng = upper_bound, lower_bound
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


def check(x: int) -> bool:
    cost = sum(a - x // f for a, f in zip(A, F) if a * f > x)
    return cost <= K


def main():
    global K, A, F
    N, K, *AF = map(int, open(0).read().split())
    A, F = AF[:N], AF[N:]
    A.sort(), F.sort(reverse=1)
    ans = binary_search()
    print(ans)


if __name__ == "__main__":
    main()