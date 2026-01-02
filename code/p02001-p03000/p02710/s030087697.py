#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect

class BIT: # binary indexed tree
    """
    http://hos.ac/slides/20140319_bit.pdf
    """

    NORMAL = 0
    ROLLBACK = 1

    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1) # var[0] is dummy
        self.status = BIT.NORMAL
        self.history = []

    def add(self, pos, val):
        assert pos > 0, pos
        if self.status == BIT.NORMAL:
            self.history.append((pos, val))
        k = pos
        while k <= self.size:
            self.data[k] += val
            # for next
            k += k & -k

    def sum(self, pos):
        s = 0
        k = pos
        while k > 0:
            s += self.data[k]
            # for next
            k -= k & -k
        return s

    def sum_section(self, frm, to):
        to_val = self.sum(to)
        frm_val = self.sum(frm)
        return to_val - frm_val

    def save(self):
        self.history = []

    def rollback(self):
        self.status = BIT.ROLLBACK
        for (pos, val) in self.history:
            self.add(pos, -1 * val)
        self.history = []
        self.status = BIT.NORMAL

class Graph:

    def __init__(self, size):
        self.size = size
        self.vertices = [0] * size # var[0] is dummy
        self.edges = [None] * size # var[0] is dummy
        for i in range(size):
            self.edges[i] = []

    def add_edge(self, frm, to):
        self.edges[frm].append(to)
        self.edges[to].append(frm)

def make_mybit(size):
    bit = BIT(size)
    for i in range(size):
        bit.add(i + 1, 1)
    bit.save()
    return bit

def init_color_s(size):
    color_s = [None] * graph.size
    for i in range(graph.size):
        color_s[i] = []
    return color_s

def dfs(graph):
    parent_s = [0] * graph.size
    in_s = [0] * graph.size
    out_s = [0] * graph.size
    order = 0 # starts from 1
    color_s = init_color_s(graph.size)
    def _dfs(v, prev):
        nonlocal order
        order += 1
        parent_s[v] = prev
        in_s[v] = order
        c = graph.vertices[v]
        color_s[c].append(v)
        for to in graph.edges[v]:
            if to == prev:
                continue
            _dfs(to, v)
        out_s[v] = order
    _dfs(0, -1)
    return parent_s, in_s, out_s, color_s

def calc(v):
    return v * (v + 1) // 2

def get_connected(bit, v, in_s, out_s):
    #print('v') # debug
    #print(v) # debug
    large_key = out_s[v]
    small_key = in_s[v] - 1
    return bit.sum_section(small_key, large_key)

def calc_for(bit, v, in_s, out_s):
    connected = get_connected(bit, v, in_s, out_s)
    #print('connected') # debug
    #print(connected) # debug
    return calc(connected)

def cut(bit, v, in_s, out_s):
    connected = get_connected(bit, v, in_s, out_s)
    bit.add(in_s[v], -1 * connected)

def solve(n, graph):
    bit = make_mybit(graph.size)
    parent_s, in_s, out_s, color_s = dfs(graph)
    #print('parent_s, in_s, out_s ') # debug
    #print(parent_s, in_s, out_s ) # debug
    #print('color_s') # debug
    #print(color_s) # debug
    for same_color_s in color_s:
        ans = calc(graph.size)
        bit.rollback()
        #print('bit.data') # debug
        #print(bit.data) # debug
        for v in same_color_s[::-1]:
            for to in graph.edges[v]:
                if to == parent_s[v]:
                    continue
                ans -= calc_for(bit, to, in_s, out_s)
            cut(bit, v, in_s, out_s)
        ans -= calc_for(bit, 0, in_s, out_s)
        #print('ans') # debug
        print(ans)






if __name__ == '__main__':
    n = int(input())
    graph = Graph(n)
    vertices = list(map(int, input().split()))
    for i, c in enumerate(vertices):
        vertices[i] = c - 1
    graph.vertices = vertices
    for _ in range(n - 1):
        frm, to = list(map(int, input().split()))
        frm -= 1
        to -= 1
        graph.add_edge(frm, to)
    solve(n, graph)


    #print('\33[32m' + 'end' + '\033[0m') # debug
