from operator import mul
from functools import reduce
from collections import Counter

def cmb(n, r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def prime_factor(n):
    ass = []
    for i in range(2, int(n ** 0.5) + 1):
        while n  % i == 0:
            ass.append(i)
            n = n // i
    if n != 1:
        ass.append(n)
    return ass

def main():
    N, M = map(int, input().split())
    num_list = prime_factor(M)
    MOD = 10 ** 9 + 7
    C = Counter(num_list)
    ans = 1
    for i, j in C.items():
        ans *= cmb(j+N-1, j)
        ans %= MOD
    print(ans)



if __name__ == "__main__":
    main()