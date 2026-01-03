#!/usr/bin/env python3
import sys
import itertools
def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    all_per = itertools.permutations(range(2,N+1))
    # 隣接行列作成
    matrix = [[0]*N for _ in range(N)]

    for aa,bb in zip(a,b):
        matrix[aa-1][bb-1] = 1
        matrix[bb-1][aa-1] = 1
    answer = 0
    for per in all_per:
        if matrix[0][per[0]-1] == 0:
            continue
        for i in range(N-2):
            if matrix[per[i]-1][per[i+1]-1] == 0:
                break
        else:
            answer += 1

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
