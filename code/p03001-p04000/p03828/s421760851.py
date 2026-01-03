import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
from collections import defaultdict
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)


def make_prime_list_2(num):
    if num < 2:
        return []

    # 0のものは素数じゃないとする
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 # 1は素数ではない
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]


def search_divisor_num_of_factorial_num(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        # 素数とその個数を入れていく
        dict_counter = defaultdict(int)
        # メモ用のdict
        dict_memo = defaultdict(list)

        for a_num in range(2, num + 1):
            num_sqrt = math.ceil(math.sqrt(a_num))
            prime_list = make_prime_list_2(num_sqrt)

            # メモ用のdictに入れるためのkeyを残しておく
            now_num = a_num

            for prime in prime_list:
                while a_num % prime == 0:
                    # メモ内にある場合、そこから全部移して、移し終わったらループを抜ける
                    if a_num in dict_memo:
                        for memo in dict_memo[a_num]:
                            dict_counter[memo] += 1
                            dict_memo[now_num].append(memo)

                        a_num = 1

                    else:
                        dict_counter[prime] += 1
                        dict_memo[now_num].append(prime)
                        a_num //= prime

            if a_num != 1:
                dict_counter[a_num] += 1
                dict_memo[now_num].append(a_num)

        divisor_num = 1
        dict_fact = dict(dict_counter)
        for value in dict_fact.values():
            divisor_num *= (value + 1)

        return divisor_num
print(search_divisor_num_of_factorial_num(_I())%mod)
