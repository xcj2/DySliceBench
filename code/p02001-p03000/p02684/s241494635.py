# -*- coding: utf-8 -*-
import sys
# sys.setrecursionlimit(10**6)
buff_readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()



class Doubling():
    def __init__(self, a0, m):
        """
        a0 is an array-like object which contains ai, 0 <= i < N.
        ai is the next value of i.
        """
        N = len(a0)
        self.N = N
        self.nt = [[None] * N for i in range(m.bit_length()+1)]
        for i, a in enumerate(a0):
            self.nt[0][i] = a

        for i in range(1, len(self.nt)):
            for j in range(N):
                if self.nt[i-1][j] is None:
                    self.nt[i][j] = None
                else:
                    self.nt[i][j] = self.nt[i-1][self.nt[i-1][j]]

    def apply(self, i, n):
        """
        Apply n times from i
        """
        j = i
        for k in range(n.bit_length()):
            m = 1 << k
            if m & n:
                j = self.nt[k][j]
            if j is None:
                break
        return j

def slv(N, K, A):
    A = [a-1 for a in A]
    d = Doubling(A, 10**18+1)
    return d.apply(0, K) + 1


def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))


if __name__ == '__main__':
    main()
