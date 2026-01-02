import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
import bisect
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**21


class Segtree_op():
    def __init__(self, n):
        self.size = 1
        while (n >= 1):
            self.size = self.size << 1
            n = n // 2

        self.arr = [self.unit() for i in range(self.size * 2)]

    def op(self, lch, rch):
        # sum
        return lch + rch

        # update min with holding index
        # if lch[0] <= rch[0]:
        #     return lch
        # else:
        #     return rch

    def unit(self):
        return 0

    def update(self, k, val):
        k += self.size - 1
        self.arr[k] = val
        while (k):
            k = (k - 1) // 2
            self.arr[k] = self.op(self.arr[k * 2 + 1], self.arr[k * 2 + 2])

    def query(self, l, r):
        L = l + self.size
        R = r + self.size
        s = self.unit()
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(s, self.arr[R - 1])

            if L & 1:
                s = self.op(s, self.arr[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return s

    # def show(self):
    #     idx = 1
    #     while (idx <= self.size):
    #         print(self.arr[idx - 1:idx * 2 - 1])
    #         idx *= 2


def main():
    n = getN()
    s = [c for c in input().strip()]
    q = getN()

    # SegTreeをa-zぶん用意する 3文字目がbならsegs[b]の3番目にフラグ1が立つ
    segs = [Segtree_op(n) for i in range(26)]
    for i, c in enumerate(s):
        segs[ord(c) - ord("a")].update(i, 1)

    for query in range(q):
        operand, a, b = input().split()
        if operand == "1":
            # 0-indexed
            a = int(a) - 1
            segs[ord(s[a]) - ord("a")].update(a, 0)
            segs[ord(b) - ord("a")].update(a, 1)
            s[a] = b

        else:  # operand == "2"
            tmp = 0
            # 0-indexed
            a, b = int(a) - 1, int(b) - 1
            for se in segs:
                # a-zそれぞれのSegTreeについて、区間内にフラグが立っていれば tmp += 1
                # 文字自体ではなくその間にindexが降られているので、右側を+1
                if se.query(a, b+1) > 0:
                    tmp += 1
            print(tmp)

    # print(segs[0].arr)

if __name__ == '__main__':
    main()

"""
7 
aaaabbb
3
1 7 c
2 1 5
2 1 7
>> 2
>> 3


26 
abcdefghijklmnopqrstuvwxyz
7
2 1 26
2 2 26
2 5 5
2 11 20
2 25 26 
1 1 z
2 1 26
>> 26
>> 25
>> 1
>> 10
>> 2
>> 25
"""