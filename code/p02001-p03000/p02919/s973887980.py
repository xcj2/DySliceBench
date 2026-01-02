# -*- coding: utf-8 -*-
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
            self.__tree[i] = operator(
                self.__tree[i * 2], self.__tree[i * 2 + 1])

    def update(self, i, v):
        i += self.__size
        self.__tree[i] = v
        while i:
            i //= 2
            self.__tree[i] = self.__op(
                self.__tree[i * 2], self.__tree[i * 2 + 1])

    def query(self, l, r):
        """[l, r)
        """
        l += self.__size
        r += self.__size
        ret = self.__ie
        while l < r:
            if l & 1:
                ret = self.__op(ret, self.__tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = self.__op(ret, self.__tree[r])
            l //= 2
            r //= 2
        return ret


@mt
def slv(N, P):
    pi = [(p, i) for i, p in enumerate(P)]
    pi.sort()
    p, i = pi.pop()
    lst = SegmentTree([-1]*N, max, -1)
    rst = SegmentTree([N]*N, min, N)
    lst.update(i, i)
    rst.update(i, i)

    ans = 0
    while pi:
        p, i = pi.pop()
        li = lst.query(0, i)
        lli = lst.query(0, li)
        ri = rst.query(i, N)
        rri = rst.query(ri+1, N)
        lst.update(i, i)
        rst.update(i, i)
        ln = (li-lli) * (ri-i)
        rn = (rri-ri) * (i-li)
        ans += ln * p
        ans += rn * p
    return ans


def main():
    N = read_int()
    P = read_int_n()
    print(slv(N, P))


if __name__ == '__main__':
    main()
