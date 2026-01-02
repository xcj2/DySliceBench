import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    chains = list(map(string_to_int, inputs))
    nodes_chain = {i+1: set() for i in range(N)}

    for c in chains:
        [a, b] = c
        nodes_chain[a].add(b)
        nodes_chain[b].add(a)

    modified = True
    count = 0
    while modified:
        modified = False
        for node1 in nodes_chain.keys():
            target_nodes = nodes_chain[node1]
            if len(target_nodes) == 1:
                node2 = target_nodes.pop()
                nodes_chain[node2].remove(node1)
                count += 1
                modified = True
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    print(ret)
