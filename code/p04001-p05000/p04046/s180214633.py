H, W, A, B = map(int, input().split())

MOD = 10 ** 9 + 7


def get_fact_list(n: int) -> list:
    result_list = [1]
    tmp = 1
    for i in range(n):
        tmp = (tmp * (i + 1)) % MOD
        result_list.append(tmp)

    return result_list


def get_inv_list(n: int, fact_lit: list) -> list:
    result_list = [1]

    for i in range(n):
        result_list.append(pow(fact_lit[i + 1], MOD - 2, MOD))

    return result_list


def comb(n: int, m: int, fact_list: list, inv_list: list) -> int:
    return (fact_list[n] * inv_list[m] * inv_list[n - m]) % MOD


h = H - A
w = W - B
ways = 0
fact = get_fact_list(H + W)
inv = get_inv_list(H + W, fact)

while h > 0 and w > 0:
    h -= 1
    w -= 1
    ways += (comb(H - A + B - 1, h, fact, inv) * comb(W + A - B - 1, w, fact, inv)) % MOD

print(ways % MOD)