import math


def get_pseudo_input():
    N = 3
    A = [6, 10, 16]
    return N, A


def get_input():
    N = int(input())
    A = [int(x) for x in input().split()]
    return N, A


def sieve_of_eratosthenes(x: int):
    ret = [-1] * (x + 1)
    for i in range(1, x + 1):
        ret[i] = i
    p_max = int(math.sqrt(x))
    for p in range(2, p_max + 1):
        if ret[p] < p:  # p is not a prime number
            continue
        for i in range(p, x + 1, p):
            if ret[i] > p:
                ret[i] = p
    return ret


A_max = 10 ** 6
p_table = sieve_of_eratosthenes(A_max)

N, A = get_input()
# Store a number of unique Ais using the prime number
p_nums = [0] * (A_max + 1)
p_nums[1] = N
max_p_nums = 0
for a in A:
    # print(f"a={a}")
    while a > 1:
        p = p_table[a]
        while a % p == 0:
            a = a // p
        # print(f"  a={a}")
        p_nums[p] += 1
        if max_p_nums < p_nums[p]:
            max_p_nums = p_nums[p]
# print(max_p_nums)
if max_p_nums <= 1:
    # GCD of A is 1
    print('pairwise coprime')
elif max_p_nums == N:
    # GCD of A is not 1
    print('not coprime')
else:
    print('setwise coprime')