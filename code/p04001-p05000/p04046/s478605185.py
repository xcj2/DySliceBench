
def read_input():
    h, w, a, b = map(int, input().split())
    return h, w, a, b


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
def reverse_mod(x):
    return power_n(x, 10**9 + 5)


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


def comb(x, y, factorial_dic):
    return factorial_dic[x] * reverse_mod(factorial_dic[y]) * reverse_mod(factorial_dic[x - y])


def path(s, e, factorial_dic, modmax):
    x = e[0] - s[0]
    y = e[1] - s[1]

    return comb(x + y, x, factorial_dic) % modmax


def submit():
    h, w, a, b = read_input()
    f_dic = factorial_table(h + w - 2)
    count = 0
    modmax = 10**9 + 7
    for i in range(h - a):
        count += path((0, 0), (i, b - 1), f_dic, modmax) * path((i, b), (h - 1, w - 1), f_dic, modmax)
        count %= modmax

    print(count)

if __name__ == '__main__':
    submit()
