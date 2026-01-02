import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect
import itertools
import heapq


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(H, W, inputs):
    d_map = inputs
    best_step_num = None
    for i in range(H):
        for j in range(W):
            process_map = [[False for _ in range(W)] for _ in range(H)]
            bfs_queue = collections.deque([[i, j, 0]])
            last_step_num = None

            while len(bfs_queue) > 0:
                [y, x, step_num] = bfs_queue.pop()
                if y >= H or x >= W or y < 0 or x < 0 or d_map[y][x] == '#' or process_map[y][x] is True:
                    continue
                process_map[y][x] = True
                last_step_num = step_num

                bfs_queue.appendleft((y+1, x, step_num+1))
                bfs_queue.appendleft((y-1, x, step_num+1))
                bfs_queue.appendleft((y, x+1, step_num+1))
                bfs_queue.appendleft((y, x-1, step_num+1))

            if last_step_num is not None and (best_step_num is None or last_step_num > best_step_num):
                best_step_num = last_step_num
    return best_step_num


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [H, W] = string_to_int(input())
    ret = solve(H, W, inputs(H))
    print(ret)
