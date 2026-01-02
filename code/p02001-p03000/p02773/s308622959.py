#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, S: "List[str]"):
    from collections import Counter
    c = Counter(S)
    ans = []
    t = c.most_common()[0][1]
    # print(t)
    for k,v in c.most_common():
        if v == t:
            ans.append(k)

    # print(ans)
    ans.sort()
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
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
