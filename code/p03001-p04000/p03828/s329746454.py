from collections import Counter


def main():
    """
    1 <= N <= 10 ** 3
    N! の正の約数の個数を10**9+7 で割った余り

    (10 ** 3)! => loopじゃ無理

    1000 * 999 * 998 * ... * 2 * 1
    →それぞれの約数を求める(1000以下なので問題なし)

    素因数分解:
    e.g. 72
        2^3 * 3^2 * 1 => 6つの要素
        6C1,6C2,6C3,6C4,6C5,6C6
        重複除外(どうする) => 6C2: 2_1,2_2と2_2,2_3

        71についても同様かつ、72の約数との組合せ => 膨大な数になる

    解説:
    ある整数 x が、素因数分解によって x = p^n × q^m × ... (p, q, ...は素数) と表せる時、
    x の約数の個数は(n + 1) × (m + 1) × ... となります。
    """
    N = int(input())

    if N == 1:
        print(1)
        return

    table = eratosthenes(N)
    factors = Counter()
    for i in range(2, N + 1):
        factors += factorize(i, table)

    ans = 1
    for count in factors.values():
        ans = ans * (count + 1) % (10 ** 9 + 7)
    print(ans)


def factorize(N, table):
    factors = Counter()
    x = N
    for i in [2] + list(range(3, N + 1, 2)):
        if table[i]:
            while x % i == 0:
                if i in factors:
                    factors[i] += 1
                else:
                    factors[i] = 1
                x = x // i

    return factors


def eratosthenes(N):
    a = [True for _ in range(N + 1)]
    a[0] = False
    a[1] = False

    for i in range(2, N + 1):
        if a[i]:
            for j in range(i + 1, N + 1):
                if j % i == 0:
                    a[j] = False

    return a

if __name__ == '__main__':
    main()
