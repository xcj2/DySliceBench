# coding: utf-8

import heapq


def calc_l_score(N, a):
    scores = [None] * (N + 1)
    queue = a[:N]
    heapq.heapify(queue)
    scores[0] = sum(queue)
    for i in range(N):
        na = a[N + i]
        heapq.heappush(queue, na)
        m = heapq.heappop(queue)
        scores[i + 1] = scores[i] + na - m
    return scores


def calc_r_score(N, a):
    scores = [None] * (N + 1)
    queue = []
    for i in range(1, N + 1):
        heapq.heappush(queue, -a[-i])
    scores[-1] = - sum(queue)
    for i in range(1, N + 1):
        na = a[-N - i]
        heapq.heappush(queue, -na)
        m = - heapq.heappop(queue)
        scores[-i - 1] = scores[-i] + na - m
    return scores


def main():
    N = int(input())
    a = list(map(int, input().split()))

    ls = calc_l_score(N, a)
    rs = calc_r_score(N, a)
    return max([l - r for l, r in zip(ls, rs)])


if __name__ == "__main__":
    print(main())
