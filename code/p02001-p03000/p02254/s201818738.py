# -*- coding: utf-8 -*-
"""
Greedy algorithms - Huffman Coding
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_15_D&lang=jp

"""
import sys
from collections import Counter

class Node:
    def __init__(self, v, f):
        self.val = v
        self.freq = f
        self.left = None
        self.right = None


def solve(s):
    res = [Node(k, v) for k, v in Counter(s).items()]
    while len(res) > 1:
        res.sort(key=lambda x: x.freq)
        z = Node('@', res[0].freq + res[1].freq)
        z.left, z.right = res[0], res[1]
        res = res[2:]
        res.append(z)

    d = dict()
    stack = [(res[0], '')]
    while stack:
        n, st = stack.pop()
        if not n.left and not n.right:
            st = '0' if not st else st
            d[n.val] = st
        if n.left:
            stack.append((n.left, st+'0'))
        if n.right:
            stack.append((n.right, st+'1'))
    return len(''.join([d[ch] for ch in s]))


def main(args):
    s = input()
    ans = solve(s)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])

