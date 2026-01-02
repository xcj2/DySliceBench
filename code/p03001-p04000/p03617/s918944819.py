# coding: utf-8
def get_ln_inputs():
    return input().split()


def get_ln_int_inputs():
    return list(map(int, get_ln_inputs()))


def main():
    prices = get_ln_int_inputs()
    N = get_ln_int_inputs()[0]
    M = N * 4

    prices_per_8litre = [prices[i] * (1 << (3 - i)) for i in range(4)]
    price_rank = [prices_per_8litre.index(price_per_8l) for price_per_8l in sorted(prices_per_8litre)]

    result = [0, 0, 0, 0]

    idx = 0
    if price_rank[idx] == 3:
        result[3] += M // 8
        M %= 8
        idx += 1
    
    cp = price_rank[idx]
    result[cp] += M // (1 << cp)

    print(sum(prices[i] * result[i] for i in range(4)))
    return


main()
