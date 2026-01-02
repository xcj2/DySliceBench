#!/usr/bin/env python3
import sys
import math
from collections import Counter
import collections
INF = float("inf")


def factorial(n):
    # 試し割りによる素因数分解
    prime_count = collections.Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1

    return prime_count


def GCD(a, b):
    if a == 0:
        return b
    else:
        return GCD(b % a, a)


def GCDs(*a):
    # リストで入力しないよう注意。
    if len(a) == 0:
        return -1  # エラー

    if len(a) == 1:
        return a[0]

    res = a[0]
    for i in range(1, len(a)):
        res = GCD(res, a[i])
    return res


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def solve(N: int, A: "List[int]"):
    c1 = make_divisors(A[0])
    c2 = make_divisors(A[1])
    c = sorted(list(set(c1 + c2)))

    OKs = []
    for cv in c:
        if sum([1 if a % cv == 0 else 0 for a in A]) >= N-1:
            OKs.append(cv)
    print(max(OKs))

    # b = A[0]
    # m = INF
    # mi = -1
    # for i in range(N):
    #     g = GCD(A[i], b)
    #     print(g)
    #     if m > g:
    #         m = g
    #         mi = i
    # buf = None
    # for i in range(N):
    #     if mi == i:
    #         continue
    #     if buf is None:
    #         buf = A[i]
    #     else:
    #         buf = GCD(buf, A[i])
    # print([buf, GCDs(*A[1:])])
    # print("回答: ", max([buf, GCDs(*A[1:])]))
    # # print(g)

    # s = SegmentTree(N)
    # for i in range(N):
    #     s.update(i, A[i])
    # # print("tree ", s.tree)
    # g = []
    # for i in range(N):
    #     # iを覗いたGCDをとる
    #     if i == 0:
    #         g.append(s.query(1, N))
    #     elif i == N-1:
    #         g.append(s.query(0, N-1))
    #     else:
    #         # print(s.query(0, i), s.query(i+1, N))
    #         g.append(GCD(s.query(0, i), s.query(i+1, N)))
    # # print(g)
    # # print("回答2: ", max(g))
    # print(max(g))

    # g = []
    # for i in range(N):
    #     buf = None
    #     for j in range(N):
    #         if i == j:
    #             continue
    #         if buf is None:
    #             buf = A[j]
    #         else:
    #             buf = GCD(buf, A[j])
    #     g.append(buf)
    # # print(g)
    # print("正解：", max(g))

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
