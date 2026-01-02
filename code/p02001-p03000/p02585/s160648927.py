#!/usr/bin/env python3
import sys
from itertools import chain


def max_add_1_to_n(loop, n):
    # print('  max_add_1_to_n', loop, n)
    l = len(loop)
    acc = loop.copy()
    # print('    ', acc)
    max_val = max(acc)
    for i in range(1, n):
        for j in range(0, l):
            acc[j] += loop[(i + j) % l]
        # print("    ", acc)
        max_val = max(max(acc), max_val)
    return max_val


def max_add_0_to_n(loop, n):
    # print('  max_add_0_to_n', loop, n)
    if n >= 1:
        return max(max_add_1_to_n(loop, n), 0)
    else:
        return 0


def max_loop_k(loop, K):
    l = len(loop)
    if K <= 2 * l:
        return max_add_1_to_n(loop, K)
    # K は 2 * l より長い
    l_sum = sum(loop)
    if l_sum <= 0:
        return max_add_1_to_n(loop, l)
    else:
        Kdiv = K // l
        Kmod = K % l
        # print('  l Kdiv Kmod', l, Kdiv, Kmod)
        return max_add_0_to_n(loop, l + Kmod) + l_sum * (Kdiv - 1)


def solve(N: int, K: int, P: "List[int]", C: "List[int]"):
    # 簡単のためインデックスを 0 からにする
    # (使用済みは -1 を入れる)
    P = [i - 1 for i in P]
    answer = -float("inf")
    for i0 in range(N):
        if P[i0] == -1:
            continue
        loop = []
        i = i0
        while P[i] != -1:
            loop.append(C[i])
            i_next = P[i]
            P[i] = -1
            i = i_next
        answer = max(answer, max_loop_k(loop, K))

    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, K, P, C)
    print(answer)


if __name__ == "__main__":
    main()
