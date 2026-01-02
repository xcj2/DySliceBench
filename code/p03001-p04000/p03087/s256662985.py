#!/usr/bin/env python3


import sys


class OccCounter(object):

    def __init__(self, n, s):
        self.length = n
        self.base_str = s
        self.occ_nums = [0] * n
        for i in range(1, n):
            self.occ_nums[i] = self.occ_nums[i - 1] + int(s[i - 1] == "A" and s[i] == "C")
        # sentinel
        self.occ_nums.insert(0, 0)
        # debug
        # print(*zip("*" + s, self.occ_nums), file=sys.stderr, sep="\n")
    
    def count_occs(self, le, ri):
        # one-based
        res = self.occ_nums[ri] - self.occ_nums[le - 1]
        if le > 1 and self.base_str[le - 2] == "A" and self.base_str[le - 1] == "C":
            res -= 1
        return res


def main():
    n, q = (int(z) for z in input().split())
    s = input()
    oc = OccCounter(n, s)
    for _ in range(q):
        le, ri = (int(z) for z in input().split())
        print(oc.count_occs(le, ri))


if __name__ == "__main__":
    main()