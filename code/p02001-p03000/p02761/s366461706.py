#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, s: "List[int]", c: "List[int]"):
    from collections import defaultdict

    d = defaultdict(list)

    for i in range(M):
        d[s[i]].append(c[i])
        d[s[i]] = list(set(d[s[i]]))

    if not all([len(v) == 1 for k, v in d.items()]):
        print('-1')
        exit()

    ans = []
    for i in range(1, N+1):
        if d[i]:
            ans.append(d[i][0])
        elif i == 1 and N >= 2:
            ans.append(1)
        else:
            ans.append(0)

    if len(str(int(''.join(map(str, ans))))) != N:
        print(-1)
    else:
        print(int(''.join(map(str, ans))))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, s, c)

if __name__ == '__main__':
    main()
