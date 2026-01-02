#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: "List[int]"):
    from collections import Counter
    import math
    from functools import lru_cache

    @lru_cache(None)
    def combination(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    
    c = Counter(A)
    
    ta = 0
    for k,v in c.items():
        if v >= 2:
            ta += combination(v, 2)
            
    # dp = [-1] * (N+1)
    ans = []
    for i in range(N):
        t = ta
        if c[A[i]] >= 2:
            t -= combination(c[A[i]], 2)
        if c[A[i]]-1 >= 2:
            t += combination(c[A[i]]-1, 2)
        
        ans.append(t)

 
    for i in ans:
        print(i)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
