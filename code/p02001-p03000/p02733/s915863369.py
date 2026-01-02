#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
h, w, k = [int(x) for x in input().split()]
s = [input() for _ in range(h)]

def add_pieces(pieces, column, ranges):
    global s
    for j in range(len(ranges)):
        L, R = ranges[j]
        pieces[j] += sum(1 for row in range(L, R) if s[row][column] == '1')

def get_ranges(mask):
    global h
    L = 0
    for i in range(h - 1):
        if mask & (1 << i):
            yield L, i + 1
            L = i + 1
    yield L, h

def cost(mask):
    global h, w, k
    ranges = list(get_ranges(mask))
    pieces = [0 for i in range(len(ranges))]
    ans = bin(mask).count('1')
    for column in range(w):
        add_pieces(pieces, column, ranges)
        if any(piece > k for piece in pieces):
            ans += 1
            pieces = [0 for i in range(len(ranges))]
            add_pieces(pieces, column, ranges)
            if any(piece > k for piece in pieces):
                return float('inf')
    return ans

print(min(cost(mask) for mask in range(1 << (h - 1))))
