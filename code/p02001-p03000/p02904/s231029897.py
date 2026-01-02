# -*- coding: utf-8 -*-
from collections import defaultdict, deque

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
def slv(N, K, P):
    min_st = SegmentTree(P, min, INF)
    max_st = SegmentTree(P, max, -1)


    a = []
    for i in range(N-K):
        min_p = min_st.query(i, i+K+1)
        max_p = max_st.query(i, i+K+1)
        if P[i] == min_p and P[i+K] == max_p:
            a.append((i, i+K))

    j = 0
    ss = []
    for i in range(N-1):
        if P[i] < P[i+1]:
            pass
        else:
            if i - j + 1>= K:
                ss.append((j, i+1))
            j = i + 1
    i += 1
    if i - j +1 >= K:
        ss.append((j, i+1))

    ans = N - K + 1
    if ss:
        ans -= sum(s[1]-s[0] - K + 1 for s in ss) - 1

    ss.reverse()
    for l, r in a:
        while ss and ss[-1][1] <= l:
            ss.pop()
        if ss:
            if ss[-1][0] <= l and r < ss[-1][1]:
                pass
            else:
                ans -= 1
        else:
            ans -= 1


    return ans

def ref(N, K, P):
    ans = set()
    for i in range(N-K+1):
        s = tuple(P[:i] + sorted(P[i:i+K]) + P[i+K:])
        ans.add(s)
        # print(s, P[:i], sorted(P[i:i+K]), P[i+K:])
    return len(ans)






def main():
    N, K = read_int_n()
    P = read_int_n()
    print(slv(N, K, P))


    # from random import randint, shuffle
    # while True:
    #     N = 100
    #     K = randint(1, N-1)
    #     P = list(range(1, N+1))
    #     shuffle(P)
    #     a = slv(N, K, P[:])
    #     b = ref(N, K, P[:])
    #     if a != b:
    #         print(N, K)
    #         print(P)
    #         print(a, b)
    #         break



if __name__ == '__main__':
    main()
