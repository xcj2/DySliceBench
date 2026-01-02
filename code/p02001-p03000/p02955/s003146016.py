import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import heapq
import bisect
import copy
import math
from collections import defaultdict, Counter

def warshall_floyd(d, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i * N +j] = min(d[i * N +j], d[i * N + k] + d[k * N + j])
    return d
MOD = 10**9 + 7
INF = 10**10

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i ** 2 != n:
                divisors.append(n // i)

    return divisors

def judge(anums, cand, k):
    anums = sorted([num % cand for num in anums])
    rem = sum([(cand - num) for num in anums])
    acc = [0]
    tmp = 0
    ue = 0
    # print(rem, anums)
    for num in anums:
        tmp += num
        acc.append(tmp)

    if acc[rem // cand] <= k:
        return True
    else:
        return False


def main():
    n,k = getlist()
    anums = getlist()

    candidates = make_divisors(sum(anums))
    # print(candidates)
    for cand in sorted(candidates, key=lambda x: -x):
        res = judge(anums, cand, k)
        if res:
            print(cand)
            return





if __name__ == '__main__':
    main()

"""
9999
3

2916
"""