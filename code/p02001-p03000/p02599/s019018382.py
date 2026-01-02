# -*- coding: utf-8 -*-
from operator import add


import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
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


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


class SegmentTree:
    def __init__(self, array, operator, identity_element):
        _len = len(array)
        self.__op = operator
        self.__size = 1 << (_len - 1).bit_length()
        self.__tree = [identity_element] * self.__size + \
            array + [identity_element] * (self.__size - _len)
        self.__ie = identity_element

        for i in range(self.__size - 1, 0, -1):
            self.__tree[i] = self.__tree[i * 2] + self.__tree[i * 2 + 1]

    def update(self, i, v):
        i += self.__size
        self.__tree[i] = v
        while i:
            i //= 2
            self.__tree[i] = self.__tree[i * 2] + self.__tree[i * 2 + 1]

    def query(self, l, r):
        """[l, r)
        """
        l += self.__size
        r += self.__size
        ret = self.__ie
        while l < r:
            if l & 1:
                ret += self.__tree[l]
                l += 1
            if r & 1:
                r -= 1
                ret += self.__tree[r]
            l //= 2
            r //= 2
        return ret

    def __getitem__(self, key):
        return self.__tree[key + self.__size]


@mt
def slv(N, Q, C, LR):
    LR.sort(key=lambda x: x[2])
    ans = [-1] * Q

    st = SegmentTree([0]*(N+1), add, 0)
    la = [-1] * (N+1)
    p = 0
    for i, l, r in LR:
        l -= 1
        r -= 1
        for j in range(p, r+1):
            c = C[j]
            if la[c] != -1:
                st.update(la[c], st[la[c]]-1)
            la[c] = j
            st.update(j, st[j]+1)
        p = r+1
        ans[i] = st.query(l, r+1)
    return ans

def main():
    N, Q = read_int_n()
    C = read_int_n()
    LR = [[_, *read_int_n()] for _ in range(Q)]
    print(*slv(N, Q, C, LR), sep='\n')

    # N = 5 * 10**5
    # Q = N
    # C = [i for i in range(1, N+1)]
    # LR = []
    # from random import randint
    # for _ in range(Q):
    #     l = randint(1, N-1)
    #     r = randint(l, N-1)
    #     LR.append([_, l, r])
    # print(*slv(N, Q, C, LR), sep='\n')



if __name__ == '__main__':
    main()
