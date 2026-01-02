import math
import random


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve2(N, A):
    gcd = A[0]
    answer = 'pairwise coprime'
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if math.gcd(A[i], A[j]) != 1:
                answer = 'setwise coprime'
            gcd = math.gcd(gcd, math.gcd(A[i], A[j]))
    if gcd > 1:
        return 'not coprime'
    return answer


def solve():
    N = read_int()
    A = read_ints()
    gcd = A[0]
    for a in A[1:]:
        gcd = math.gcd(gcd, a)
    if gcd > 1:
        return 'not coprime'

    is_prime = [True]*(10**6+1)
    B = [False]*(10**6+1)
    for a in A:
        if B[a] and a > 1:
            return 'setwise coprime'
        B[a] = True

    for p in range(2, 10**6+1):
        if is_prime[p]:
            count = B[p]
            for q in range(2*p, 10**6+1, p):
                is_prime[q] = False
                count += B[q]
            if count > 1:
                return 'setwise coprime'
    return 'pairwise coprime'


if __name__ == '__main__':
    print(solve())
