#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(N: int, p: "List[int]"):
    s = list(range(1, N + 1))
    cnt = 0
    for i in range(N):
        if s[i] != p[i]:
            cnt += 1
    if cnt == 0 or cnt == 2:
        ret = YES
    else:
        ret = NO

    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, p)

if __name__ == '__main__':
    main()
