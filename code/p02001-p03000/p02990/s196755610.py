
def solve_commentary():
    N, K = map(int, input().split())
    R = N - K  # 赤玉の数
    MOD = 10 ** 9 + 7
    for i in range(1, K + 1):
        if N - K + 1 >= i:
            print((combinations_count(N - K + 1, i) * combinations_count(K - 1, i - 1)) % (MOD))
        else:
            print(0)
        pass
    pass


def combinations_count(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def ppprint(itr_obj):
    for ite in itr_obj:
        print(ite)


if __name__ == '__main__':
    # solve()
    solve_commentary()
