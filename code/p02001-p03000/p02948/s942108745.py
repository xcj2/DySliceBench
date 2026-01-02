#!/usr/bin/env python3
import sys, heapq
sys.setrecursionlimit(300000)


def solve(N: int, m: int, A: "List[int]", B: "List[int]"):
    p = []
    for i in range(N):
        p.append([A[i], B[i]])
    p.sort(key = lambda x: (x[0], - x[1]))
    #print(p)
    ret = 0
    tmp = 1
    idx = 0
    q = []
    while tmp <= m:
        while idx < len(p) and p[idx][0] <= tmp:
            heapq.heappush(q, -p[idx][1])
            idx += 1
        #print(q)
        if len(q) > 0:
            head = heapq.heappop(q)
            ret += -head
        tmp += 1
    print(ret)
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
