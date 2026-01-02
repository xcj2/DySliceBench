#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, s: "List[str]"):
    l = [''.join(sorted(list(i))) for i in s]
    from collections import Counter
    c = Counter(l)

    import math
    def combination(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    ans = 0
    for k, v in c.most_common():
        if v >= 2:
            ans += combination(v, 2)

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()
