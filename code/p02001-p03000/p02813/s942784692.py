#from math import sqrt
#from heapq import heappush, heappop
#from collections import deque

#a, b = [int(v) for v in input().split()]


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    fullbit = (1 << N) - 1

    def full(ary, val, bit, ret):
        if bit == fullbit:
            ret.append(val)
            return
        for i in range(N):
            if bit & (1 << i) == 0:
                full(ary, val * 10 + ary[i], bit | (1 << i), ret)

    def to_i(ary):
        n = 0
        for v in ary:
            n = n * 10 + v
        return n

    def index_of(ary, val):
        lower = 0
        upper = len(ary) - 1
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            v = ary[mid]
            if v < val:
                lower = mid + 1
            elif v > val:
                upper = mid - 1
            else:
                return mid

        return lower

    ret1 = []
    full(P, 0, 0, ret1)
    ret1.sort()
    a = index_of(ret1, to_i(P))

    ret2 = []
    full(Q, 0, 0, ret2)
    ret2.sort()
    b = index_of(ret2, to_i(Q))

    print(abs(a - b))


main()
