#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(K: int):
    def _make(s, idx):
        if idx > 0:
            if s[idx] == '9':
                return None
            prev = int(s[idx - 1])
            cur  = int(s[idx]) + 1
            if abs(prev - cur) > 1:
                return None
        if idx == 0 and s[idx] == '9':
            return '1' + ('0' * len(s))

        ret = s[:idx]
        ret += str(int(s[idx]) + 1)
        for _ in s[idx + 1:]:
            ret += str(max(0, int(ret[-1]) - 1))
        return ret

    def get_next(s):
        idx = 0
        l = len(s)
        for idx in range(l)[::-1]:
            tmp = _make(s, idx)
            if tmp is not None:
                return tmp
        return None

    val = '0'
    for i in range(K):
        val = get_next(val)
    print(val)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()
