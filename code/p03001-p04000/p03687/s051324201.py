#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(s: str):
    from collections import Counter
    c = Counter(s)

    N = len(s)
    ans = INF


    for k in c.keys():
        c = 0
        sc = s
        for j in range(N):
            ls = []
            for i in range(len(sc)-1):
                if sc[i] == k or sc[i+1] == k:
                    ls.append(k)
                else:
                    ls.append(sc[i])
            c += 1
            
            if all([j == k for j in sc]):
                break

            sc = ''.join(ls)
        ans = min(ans, c-1)

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
