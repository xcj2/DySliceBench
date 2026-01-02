

# xの階乗 mod 10**9 + 7 について、1~nまでの結果を辞書にして返す
def factorial_table(n):
    result = {0:1}

    curr = 1
    acc = 1
    modmax = (10**9) + 7
    while curr <= n:
        acc *= curr
        acc %= modmax
        result[curr] = acc
        curr += 1

    return result

# xの逆元 mod 10**9 + 7を求める
def reverse_mod(x, rev_table):
    if x in rev_table.keys():
        return rev_table[x]

    rev_table[x] = power_n(x, 10**9 + 5)
    return rev_table[x]


# xのn乗 mod 10**9 + 7を求める
def power_n(x, n):
    r = 1
    curr_a = x
    modmax = (10 ** 9) + 7
    while n:
        if 1 & n:
            r *= curr_a
            r %= modmax

        n = n >> 1
        curr_a *= curr_a
        curr_a %= modmax

    return r


def factorial(n, fact_table):
    return fact_table[n]


def combination(n, k, fact_table, combi_table, rev_table):
    if (n, k) in combi_table.keys():
        return combi_table[(n, k)]

    combi_table[(n, k)] = factorial(n, fact_table) * \
        reverse_mod(factorial(k, fact_table), rev_table) * \
        reverse_mod(factorial(n - k, fact_table), rev_table) % (10**9 + 7)
    return combi_table[(n, k)]


def read_input():
    n, k = map(int, input().split())
    return n, k


def submit():
    n, k = read_input()

    md = 10 ** 9 + 7

    # 階乗を求めておく
    fact_table = factorial_table(n)

    # 逆元を求めておく
    rev_table = {}
    for i in range(n + 1):
        reverse_mod(i, rev_table)

    r = n - k
    combi_table = {}

    print(r + 1)

    for i in range(2, k + 1):
        inner_sum = 0
        for s in range(i - 1, r + 1):
            red_divided = combination(s - 1, i - 2, fact_table, combi_table, rev_table)
            inner_sum += (r - s + 1) * red_divided
            inner_sum %= md

        blue_divided = combination(k - 1, i - 1, fact_table, combi_table, rev_table)
        ans = blue_divided * inner_sum % md
        print(ans)

    return


if __name__ == '__main__':
    submit()
