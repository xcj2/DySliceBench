from collections import defaultdict


def is_prime(n: int)-> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    # when n is a prime number
    # x^(n-1) ≡ 1 (mod n)
    return pow(2, (n-1), n) == 1


def prime_factorize(n: int):
    prime_factors = []
    range_max = int(n //2) + 1

    for i in range(2, range_max):
        if not is_prime(i):
            continue
        while True:
            div, mod = divmod(n, i)
            if mod == 0:
                prime_factors.append(i)
                n = div
            else:
                break
        if n == 1:
            break
    prime_factors.append(n)
    return prime_factors


prime_factors_dict = {0: {}}

def main():
    n = int(input())

    for i in range(1,n+1):
        prime_factors = prime_factorize(i)
        this_prime_factors = defaultdict(int)
        for pm in prime_factors:
            this_prime_factors[pm] += 1

        for k, v in prime_factors_dict[i-1].items():
            this_prime_factors[k] += v
        prime_factors_dict[i] = this_prime_factors

    this_prime_factors = prime_factors_dict[n]

    prime_factors_list = sorted(list(filter(lambda x:x[0] != 1, this_prime_factors.items())))

    cnt_mt_74times = len(list(filter(lambda x: x[1] >= 74, prime_factors_list)))
    cnt_mt_24times = len(list(filter(lambda x: x[1] >= 24, prime_factors_list)))
    cnt_mt_14times = len(list(filter(lambda x: x[1] >= 14, prime_factors_list)))
    cnt_mt_4times  = len(list(filter(lambda x: x[1] >= 4, prime_factors_list)))
    cnt_mt_2times  = len(list(filter(lambda x: x[1] >= 2, prime_factors_list)))

    ans_cnt = 0

    # q^74
    ans_cnt += cnt_mt_74times

    # q^24 * p^2
    ans_cnt += cnt_mt_24times * (cnt_mt_2times - 1)

    # q^14 * p^4
    ans_cnt += cnt_mt_14times * (cnt_mt_4times - 1)

    # q^4 * p^4 * r^2
    ans_cnt += cnt_mt_4times * (cnt_mt_4times - 1) // 2 * (cnt_mt_2times - 2)

    print(ans_cnt)

    return



main()