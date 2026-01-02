# -*- coding: utf-8 -*-
import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_str():
    return readline().strip()


def slv(N, X):
    C = X.count('1')
    cmr = 0
    cpr = 0
    for b in X:
        b = int(b)
        cpr = ((cpr * 2) + b) % (C+1)
        if C-1 != 0:
            cmr = ((cmr * 2) + b) % (C-1)

    ans = []
    for i in range(N):
        t = 1
        if X[i] == '0':
            x = (cpr + pow(2, N-i-1, C+1)) % (C+1)
        elif X[i] == '1' and C-1 != 0:
            x = (cmr - pow(2, N-i-1, C-1)) % (C-1)
        else:
            x = 0
            t = 0

        while x != 0:
            x %= bin(x).count('1')
            t += 1

        ans.append(t)

    return ans


def main():
    N = read_int()
    X = read_str()
    print(*slv(N, X), sep='\n')


if __name__ == '__main__':
    main()
