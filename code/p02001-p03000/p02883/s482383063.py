def binary_search(*, ok, ng, func):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N, K = map(int, input().split())
    *A, = sorted(map(int, input().split()))
    *F, = sorted(map(int, input().split()), reverse=True)

    def is_ok(score):
        rest = K
        for a, f in zip(A, F):
            exceed = max(0, a * f - score)
            if exceed:
                need = (exceed + f - 1) // f
                if need > a or need > rest:
                    return False
                rest -= need
        return True

    ans = binary_search(ok=10 ** 12, ng=-1, func=is_ok)
    print(ans)


if __name__ == '__main__':
    main()
