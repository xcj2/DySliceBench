#!/usr/bin/env python3

import sys

DEBUG = False


class SegmentTree:

    # Use 1-based index internally
    def __init__(self, n, merge_func, fillval=sys.maxsize):
        self.n = 1
        while self.n < n:
            self.n *= 2
        self.nodes = [fillval] * (self.n * 2 - 1 + 1)  # +1 for 1-based index
        self.merge_func = merge_func
        self.fillval = fillval
    
    def update(self, idx, val):
        idx += 1  # for 1-based index

        nodes = self.nodes
        mergef = self.merge_func

        idx += self.n - 1
        nodes[idx] = val
        while idx > 1: # > 1 for 1-based index
            idx >>= 1  # parent(idx) = idx >> 1 for 1-based index segment tree
            nodes[idx] = mergef(nodes[idx << 1], nodes[(idx << 1) + 1]) # child(idx) = idx << 1 and idx << 1 + 1
    
    def query(self, l, r):
        l += 1; r += 1  # for 1-based index

        l += self.n - 1
        r += self.n - 1
        acc = self.fillval
        while l < r:
            if l & 1:
                acc = self.merge_func(acc, self.nodes[l])
                l += 1
            if r & 1:
                acc = self.merge_func(acc, self.nodes[r - 1])
                r -= 1
            l >>= 1
            r >>= 1
        return acc

def read(t = str):
    return t(sys.stdin.readline().rstrip())

def read_list(t = str, sep = " "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    read()
    s = read()

    a_ord = ord("a")
    bit_offsets = {chr(c_ord): c_ord - a_ord for c_ord in range(ord("a"), ord("z") + 1)}

    apps = SegmentTree(len(s), lambda x, y: x | y, 0)
    i = 0
    for c in s:
        apps.update(i, 1 << bit_offsets[c])
        i += 1

    nr_q = read(int)
    for i in range(0, nr_q):
        q = read_list()
        if q[0] == "1":
            _, i, c = q  # i_q in the question starts from 1, not 0
            apps.update(int(i) - 1, 1 << bit_offsets[c])
        else:
            _, l, r = q  # l_q and r_q in the question start from 1, not 0
            print(bin(apps.query(int(l) - 1, int(r) - 1 + 1)).count("1"))  # query in the question includes both edges


if __name__ == "__main__":
    main()