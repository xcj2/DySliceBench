from sys import stdin, setrecursionlimit
from collections import Counter, deque, defaultdict
from math import floor, ceil
from bisect import bisect_left
from itertools import combinations
setrecursionlimit(100000)

INF = int(1e10)
MOD = int(1e9 + 7)

def naive(N, X, M):
    ans = X
    ans_prev = X
    for i in range(2, N + 1):
        an1 = ans_prev % M
        an1 = pow(an1, 2, M)
        ans += an1
        ans_prev = an1
    return ans

def doubling(N, X, M):
    ans = X
    ans_prev = X
    A = [X]
    computed = set({})

    for i in range(2, N + 1):
        an1 = ans_prev % M
        an1 = pow(an1, 2, M)
        if an1 in computed:
            breakA = an1
            break
        A.append(an1)
        computed.add(an1)
        ans_prev = an1

    # if break
    num_break = len(A)
    index = A.index(breakA)
    num_length = len(A) - index
    total = sum(A[:index])
    repeat_length = (N - index) // num_length
    remain_length = (N - index) % num_length
    total_sub = sum(A[index:]) * repeat_length
    total += total_sub
    if remain_length > 0:
        sub = naive(remain_length, breakA, M)
        total += sub    
    return total


def solve(N, X, M):
    return -1

def main():
    from builtins import int, map
    N, X, M = map(int, input().split())

    if N < 10 ** 7:
        print(naive(N, X, M))
    else:
        print(doubling(N, X, M))
        # print(naive(N, X, M))

if __name__ == '__main__':
    main()
