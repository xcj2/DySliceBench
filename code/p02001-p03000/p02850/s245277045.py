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


def solve(inputs):
    chain_inputs = list(map(string_to_int, inputs))

    CHAIN_N = len(inputs)
    NODE_N = CHAIN_N + 1

    # {node: {target: chain_index}}
    node_relation = {i: {} for i in range(NODE_N)}
    # {index: color}
    chain_color = {i: None for i in range(CHAIN_N)}
    # {node : set(color)}
    node_has_color = {i: set() for i in range(NODE_N)}
    passed = set()

    for i, c in enumerate(chain_inputs):
        node = c[0] - 1
        target = c[1] - 1
        node_relation[node][target] = i
        node_relation[target][node] = i

    bfs_queue = collections.deque([0])

    max_branch = 0
    while len(bfs_queue) > 0:
        node = bfs_queue.pop()
        leafs = node_relation[node]
        if max_branch < len(leafs):
            max_branch = len(leafs)

        color = 1
        for leaf, index in leafs.items():
            if leaf in passed:
                continue
            # search color
            # while color in node_has_color[node] or color in node_has_color[leaf]:
            while color in node_has_color[node]:
                color += 1
            node_has_color[node].add(color)
            node_has_color[leaf].add(color)
            chain_color[index] = color

            bfs_queue.appendleft(leaf)
            passed.add(node)

    ret = [max_branch]
    for i in range(CHAIN_N):
        ret.append(chain_color[i])
    return ret


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N-1))
    for r in ret:
        print(r)
