#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]"):
    ans = 0
    c = 1
    n = a[0]
    for i in range(1, N):
        # print(c)
        if a[i] == n:
            c += 1
            continue
        else:
            if c >= 2:
                ans += c//2
                
            n = a[i]
            c = 1

    if c >= 2:
        n = a[i]
        ans += c//2

    
    print(ans)

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
