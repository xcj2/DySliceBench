# coding: utf-8
INF = 10 ** 20
MOD = 10 ** 9 + 7


def II(): return int(input())


def ILI(): return list(map(int, input().split()))


def read():
    N = II()
    a = ILI()
    return (N, a)


def check_a(N, a):
    for _a in a:
        if _a >= N:
            return False
    return True


def solve(N, a):
    ans = 0
    while True:
        if check_a(N, a):
            break

        l_div, l_mod = [None] * N, [None] * N
        for i, _a in enumerate(a):
            l_div[i], l_mod[i] = divmod(_a, N)

        sum_div = sum(l_div)
        for i in range(N):
            a[i] = l_mod[i] + sum_div - l_div[i]

        ans += sum_div

    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
