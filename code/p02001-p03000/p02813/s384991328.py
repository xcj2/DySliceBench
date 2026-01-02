#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, P: "List[int]", Q: "List[int]"):
    
    from itertools import combinations, permutations
    ans = [''.join(list(map(str, list(v)))) for v in permutations(P, N)]
    ans.sort()
    a = ans.index(''.join(list(map(str, P))))
    b = ans.index(''.join(list(map(str, Q))))
    print(abs(a-b))
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q)

if __name__ == '__main__':
    main()
