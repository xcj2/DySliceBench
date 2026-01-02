#!/usr/bin/env python3
import sys
import heapq

def solve(X: int, Y: int, Z: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    A = sorted(A,reverse = True)
    B = sorted(B,reverse = True)
    C = sorted(C,reverse = True)

    d = []
    heapq.heappush(d, (-(A[0]+B[0]+C[0]), 0, 0, 0)) # heapqにタプルを与えると最初の要素でソートする
    ijk_set = set((0,0,0))

    for _ in range(K):
        tmp, i, j, k = heapq.heappop(d)
        print(-tmp)
        if (i+1,j,k) not in ijk_set and i+1 <= X-1:
            heapq.heappush(d, (-(A[i+1]+B[j]+C[k]), i+1, j, k))
            ijk_set.add((i+1,j,k))
        if (i,j+1,k) not in ijk_set and j+1 <= Y-1:
            heapq.heappush(d, (-(A[i]+B[j+1]+C[k]), i, j+1, k))
            ijk_set.add((i,j+1,k))
        if (i,j,k+1) not in ijk_set and k+1 <= Z-1:
            heapq.heappush(d, (-(A[i]+B[j]+C[k+1]), i, j, k+1))
            ijk_set.add((i,j,k+1))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(X)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(Y)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(Z)]  # type: "List[int]"
    solve(X, Y, Z, K, A, B, C)

if __name__ == '__main__':
    main()
