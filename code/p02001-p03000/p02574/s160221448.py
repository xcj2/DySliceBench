import math
from functools import reduce
from collections import defaultdict


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_max = max(A)

    is_pairwise_coprime = True

    D = [-1] * (A_max + 1)
    for i in range(2, A_max + 1):
        if D[i] == -1:
            D[i] = i
            for j in range(i*i, A_max+1, i):
                D[j] = i

    def factorization(n):
        # assert 0 < n <= A_max
        primes_ = defaultdict(int)
        temp = n
        while temp > 1:
            primes_[D[temp]] += 1
            temp = temp // D[temp]

        return primes_

    P = [False]*(A_max+1)

    # primes = set({})
    for i in range(N):
        for p in factorization(A[i]).keys():
            # if p in primes:
            if P[p]:
                is_pairwise_coprime = False
                break
            else:
                # primes.add(p)
                P[p] = True

    gcd_ = reduce(math.gcd, A)

    if is_pairwise_coprime:
        print('pairwise coprime')
    elif gcd_ == 1:
        print('setwise coprime')
    else:
        print('not coprime')


if __name__ == '__main__':
    main()
