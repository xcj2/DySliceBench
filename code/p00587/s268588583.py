#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def tree_left(node, it):
    c = next(it)

    if c == "(":
        node[0] = [None, None]
        tree_left(node[0], it)
        c = next(it)

    if c == ",":
        tree_right(node, it)
    else:
        assert False

def tree_right(node, it):
    c = next(it)

    if c == "(":
        node[1] = [None, None]
        tree_left(node[1], it)
        c = next(it)

    if c == ")":
        pass
    else:
        assert False

def tree_parse(s):
    root = [None, None]

    s = s[1:]
    it = iter(s)
    tree_left(root, it)

    return root

def tree_dump(node):
    s = ""

    s += "("
    if node[0]:
        s += tree_dump(node[0])
    s += ","
    if node[1]:
        s += tree_dump(node[1])
    s += ")"

    return s

def intersection(t1, t2):
    if t1 is None or t2 is None:
        return None

    node = [None, None]
    node[0] = intersection(t1[0], t2[0])
    node[1] = intersection(t1[1], t2[1])
    return node

def union(t1, t2):
    if t1 is None and t2 is None:
        return None
    elif t1 is None:
        return t2
    elif t2 is None:
        return t1

    node = [None, None]
    node[0] = union(t1[0], t2[0])
    node[1] = union(t1[1], t2[1])
    return node

def main():
    for line in sys.stdin:
        op, s1, s2 = line.split()
        tree1 = tree_parse(s1)
        tree2 = tree_parse(s2)
        #print(tree_dump(tree1))
        #print(tree_dump(tree2))
        if op == "i":
            ans = intersection(tree1, tree2)
            print(tree_dump(ans))
        elif op == "u":
            ans = union(tree1, tree2)
            print(tree_dump(ans))

if __name__ == "__main__": main()