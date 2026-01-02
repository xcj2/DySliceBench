import sys
import math
import collections
import itertools
import array
import inspect
import copy

# Set max recursion limit
sys.setrecursionlimit(10000)

# Debug output
def chkprint(*args):
    names = {id(v):k for k,v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

# Binary converter
def to_bin(x):
    return bin(x)[2:]

# Set 2 dimension list
def dim2input(N):
    li = []
    for _ in range(N):
        li.append(input().split())
    return li

# --------------------------------------------

dp = None

def A_is_connected(A, edge, n_V):
    A[edge[0]][edge[1]] = False
    A[edge[1]][edge[0]] = False

    queue = [1]
    reached = [1]

    while len(queue) != 0:
        new_queue = []
        for q in queue:
            for i, is_connected in enumerate(A[q]):
                if is_connected and i not in reached:
                    new_queue.append(i)
                    reached.append(i)

        queue = new_queue

    return len(reached) == n_V


def main():
    n_V, n_E = list(map(int, input().split()))

    A = []
    for i in range(n_V+1):
        A.append([])
        for j in range(n_V+1):
            A[i].append(False)

    edges = []
    for _ in range(n_E):
        edges.append(list(map(int, input().split())))

    for edge in edges:
        A[edge[0]][edge[1]] = True
        A[edge[1]][edge[0]] = True

    n_bridge = 0

    for edge in edges:
        origin_A = copy.deepcopy(A)
        if not A_is_connected(A, edge, n_V):
            n_bridge += 1
        A = origin_A

    print(n_bridge)


main()
