#!/usr/bin/env python3
import sys

M = 'zzzzzz'

def dfs(s, K, N, r, a, ss):
    m = a[r]
    for i in range(N):
        if s[i] == m:
            t = ''
            for j in range(i, min(i+K, N)):
                t += s[j]
                if t in ss:
                    continue
                if t >= ss[-1]:
                    break
                ss.pop()
                ss.append(t)
                list.sort(ss)
    if ss[-1] == M:
        return dfs(s, K, N, r+1, a, ss)
    return ss[-1]


def solve(s: str, K: int):
    ss = [M] * K
    a = sorted(list(set(s)))
    N = len(s)
    return dfs(s, K, N, 0, a, ss)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)
    K = int(next(tokens))
    print(solve(s, K))

if __name__ == '__main__':
    main()
