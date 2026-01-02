#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 2  # type: int

def solve(N: int, a: "List[int]"):
    a = [0] + a
    b = [0] * (N+1)
    for i in range(N,0,-1):
        j = i*2
        n = 0
        while j <= N:
            n += b[j]
            j += i
        # print("a[i],n :", i, a[i], n)
        if a[i] == n%MOD:
            b[i] = 0
        else:
            b[i] = 1

    x = [i for i in range(1, N+1) if b[i] == 1]
    print(len(x))
    for i in x:
        print(i)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
