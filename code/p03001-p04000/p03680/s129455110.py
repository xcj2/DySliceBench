#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]"):
    used = [False] * (N + 1)
    ret = -1
    cnt = 1
    a = [0] + a
    tmp = a[1]
    while True:
        if tmp == 2:
            ret = cnt
            break
        if used[tmp]:
            break
        else:
            used[tmp] = True
            cnt += 1
            tmp = a[tmp]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
