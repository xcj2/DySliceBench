#!/usr/bin/env python3
import sys


def solve(n, m, s, p):
    ret = 0
    #print(s)
    #print(p)
    count = 0
    for bits in range(2 ** n):
        ok = True
        for j in range(m):
            count = 0
            for i in s[j]:
                if (bits & (1 << (i - 1))) > 0:
                    count += 1
            #        print(count)
            #        print('jk')
            #    print(bits, j, count)
            #print('--- count : ', count, j, p[j])
            #print(bits, j, count, p[j])
            if count % 2 != p[j]:
                ok = False
                break
        #print(bits)
        #print(ok)
        #print()
        if ok:
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [[] for _ in range(M)]
    for i in range(M):
        n = int(next(tokens))
        for j in range(n):
            s[i].append(int(next(tokens)))
    p = []
    for i in range(M):
        p.append(int(next(tokens)))
    solve(N, M, s, p)

if __name__ == '__main__':
    main()
