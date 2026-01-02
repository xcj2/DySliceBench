import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()
from math import sqrt


def factor(n):
    """
    nの約数を個数と共にリストにして返す。
    ただしあとの都合上１は除外する。
    """

    if n == 1:
        return 0, []
    if n == 2:
        return 1, [2]
    if n == 3:
        return 1, [3]

    d = int(sqrt(n))
    num = 1
    factor_pre = []
    factor_post = [n]
    for i in range(2, d):
        if n % i == 0:
            factor_pre.append(i)
            factor_post.append(n // i)
            num += 2
    if d * d == n:
        factor_pre.append(d)
        num += 1
    elif n % d == 0:
        factor_pre.append(d)
        factor_post.append(n // d)
        num += 2
    factor_post.reverse()
    return num, factor_pre + factor_post


def main():
    N = int(input())

    """
    題を満たすKは、
        N = K^e * n、(n, K) = 1
    として
        n = K * m + 1 (m ¥in ¥mathbb{N})
    とかければ良い。

    ２つ目の式からnとKが互いに素なのは明らかなので、問題文は
        N = K^e * (K * m + 1) (m ¥in ¥mathbb{N})
    なるKを求めることに同値。

    なのでまずはNの約数を全列挙して、あとはNをそれで割った商がKで割って1余るか確かめれば良い。
    """

    _, fact = factor(N)
    ans, ans_list = factor(N - 1)
    # print(ans_list)

    # print("Now we check the list {}".format(fact))
    for K in fact:
        n = N
        while n % K == 0:
            n //= K
        if n % K == 1:
            ans += 1
            ans_list.append(K)
            # print("{} added".format(K))
    # print("ans={}: {}".format(ans, ans_list))
    print(ans)



if __name__ == "__main__":
    main()
