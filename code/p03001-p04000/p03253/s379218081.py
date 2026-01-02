from operator import mul
from functools import reduce

MOD = 10 ** 9 + 7

def get_soinnsuu(num):
    soinnsuu = []
    for i in range(2, int(num ** 0.5) + 2):
        now_time = 0
        if num < i:
            break
        while num % i == 0:
            now_time += 1
            num = num // i
        if now_time > 0:
            soinnsuu.append(now_time)
    if num > 1:
        soinnsuu.append(1)
    return soinnsuu


def comb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


def start_process(N, M):
    soinnsuu = get_soinnsuu(M)
    ans = 1
    for ele in soinnsuu:
        ans *= int(comb(ele + N - 1, ele))
    # print(soinnsuu)
    print(ans % MOD)


def main():
    N, M = map(int, input().split())
    start_process(N, M)



if __name__ == '__main__':
    main()
