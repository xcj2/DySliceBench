#!/usr/bin/env python3
import sys
import heapq
INF = float("inf")


class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    # 後ろから貪欲
    AB = list(zip(A, B))
    AB.sort()
    A, B = zip(*AB)
    DP = [0]
    h = MaxHeap([])
    left = 0
    for i in range(1, M+1):
        while left < N and A[left] <= i:
            h.push(B[left])
            left += 1
        if len(h) > 0:
            # print("h", h)
            b = h.pop()
            # print(b, DP[-1]+b)
            DP.append(DP[-1]+b)
        else:
            DP.append(DP[-1])
    print(DP[-1])
    # print(DP)
    # print(h)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == '__main__':
    main()
