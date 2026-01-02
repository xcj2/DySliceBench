#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    p = []
    for i in range(M):
        p.append([B[i], C[i]])
    p.sort(reverse=True, key=lambda x: x[1])
    ret = 0
    cnt = 0
    A.sort()
    for q in p:
        while cnt < N and q[1] > A[cnt] and q[0] > 0:
            ret += q[1]
            cnt += 1
            q[0] -= 1
        if cnt >= N or (q[0] > 0 and q[1] <= A[cnt]):
            break
    if cnt < N:
        ret += sum(A[cnt:])
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
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]" 
    C = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
