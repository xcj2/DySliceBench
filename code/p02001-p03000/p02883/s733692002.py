# https://atcoder.jp/contests/abc144/submissions/8168248
# is_okでscoreを割るアイディア

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
            max_a = score // f
            rest -= max(0, a - max_a)
            if rest < 0: return False
        return True

    ans = binary_search(ok=10 ** 12, ng=-1, func=is_ok)
    print(ans)


if __name__ == '__main__':
    main()
