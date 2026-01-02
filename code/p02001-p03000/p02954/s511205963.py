#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(S: str):
    n = len(S)
    ret = [0] * n
    cur = 'R'
    cnt = 1
    r_idx = 0
    for i in range(1, n):
        c = S[i]
        if c == cur:
            cnt += 1
        elif c == 'L':
            l_idx = i
            cur = 'L'
        else:
            r = l_idx - r_idx
            l = i - l_idx
            ret[l_idx - 1] = (r // 2) + r % 2 + (l // 2)
            ret[l_idx] = (r // 2) + (l // 2) + l % 2 
            r_idx = i
            cnt = 1
            cur = 'R'
    r = l_idx - r_idx
    l = n - l_idx
    ret[l_idx - 1] = (r // 2) + r % 2 + (l // 2)
    ret[l_idx] = (r // 2) + (l // 2) + l % 2 
    print(' '.join([str(r) for r in ret]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
