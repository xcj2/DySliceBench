import numpy as np


def calc_mul4_dp(n, aaa):
    # result[i] = aaa[i] 以右をascendingにするために4をかける必要のある回数

    # 「支配的」である数と位置を記録するstack
    # 支配的: それを4倍すると、それより右で次に支配的な数までは全て4倍する必要のある数
    # (支配的な数, ←をいじらなかった場合の支配区間の最後の数, 最初の数の位置)
    # 第2項は巨大になり得るが、A_iの最大値 10^9 を超えたら常に末尾までが支配区間となるので、適当に上限でclip
    stack = [(10 ** 12, 10 ** 12, n), (aaa[-1], aaa[-1], n - 1)]
    INF = 10 ** 11
    result = [0, 0]

    for i in range(n - 2, -1, -1):
        a = aaa[i]
        c = a
        inc = 0
        while (c << 2) > stack[-1][0]:
            b, e, j = stack.pop()
            mul = 0
            while c > b:
                b <<= 2
                mul += 1
            inc += mul * (stack[-1][2] - j)
            c = min(e << (2 * mul), INF)
        stack.append((a, c, i))
        result.append(inc)
        # print(a, stack, result)
    result = np.add.accumulate(result, dtype=np.int64)[::-1]
    return result


def solve(n, aaa):
    fdp = calc_mul4_dp(n, aaa)
    bdp = calc_mul4_dp(n, aaa[::-1])[::-1]
    # print(fdp)
    # print(bdp)
    return ((fdp + bdp) * 2 + np.arange(n + 1, dtype=np.int64)).min()


def test():
    import random
    n = 200000
    # aaa = random.choices(range(1, 10 ** 9), k=n)
    # aaa = [1, 10 ** 9] * (n // 2)
    aaa = list(range(10 ** 9, 10 ** 9 - n, -1))
    print(n)
    # print(aaa)
    print(solve(n, aaa))


# test()

n = int(input())
aaa = list(map(int, input().split()))
print(solve(n, aaa))
