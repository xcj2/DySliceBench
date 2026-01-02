#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32
import heapq

# refer to https://atcoder.jp/contests/abc137/submissions/6814694

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    from collections import defaultdict
    d = defaultdict(list)

    for i in range(N):
        d[A[i]].append(-B[i])

    h = []
    res = 0
    heapq.heapify(h)

    # i日以下で追加できるものを追加していく
    # 　⇒「editorialの後ろから見ていく」になる
    for i in range(1, M+1):
        # ちょうどi日で実施できるものの候補をすべてpushする
        if d[i]:
            for v in d[i]:
                heapq.heappush(h, v)
        
        # でもその日に実行できるバイトは一つだけなので、一つを取り出す。
        # こうするとi+1...のときに、参照されなかったものも候補になる
        if h:
            res += heapq.heappop(h)
        
        # print(i, h, res)

    print(-res)

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
