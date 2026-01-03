#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    p = []
    for i in range(N):
        p.append([a[i], b[i]])
    p.sort(key=lambda x:x[0])
    tmp = 0
    ret = 0
    for v, c in p:
        tmp += c
        if K <= tmp:
            ret = v
            break
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]" 
    b = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, K, a, b)

if __name__ == '__main__':
    main()
