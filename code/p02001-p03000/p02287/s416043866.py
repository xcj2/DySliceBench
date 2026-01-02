#! /usr/bin/env python


def print_heap (heap, i):
    ret = "node {0}: key = {1}, ".format(i + 1, heap[i])

    p = get_parent_node(i)
    if p is not None:
        ret += "parent key = {0}, ".format(heap[p])

    len_heap = len(heap)
    l = get_left_node(i)
    r = get_right_node(i)

    if l < len_heap:
        ret += "left key = {0}, ".format(heap[l])
    if r < len_heap:
        ret += "right key = {0}, ".format(heap[r])

    print(ret)
    return

def get_parent_node (i):
    p = (i - 1) // 2
    if p < 0:
        return None
    else:
        return p

def get_left_node (i):
    l = (i + 1) * 2 - 1
    return l

def get_right_node (i):
    r = (i + 1) * 2
    return r

def proc_inputs ():
    num_inputs = int(input())
    inputs = [i for i in input().split()]
    return num_inputs, inputs



def main ():
    num_inputs, inputs = proc_inputs()
    heap = [None] * num_inputs
    for i, node in enumerate(inputs):
        heap[i] = node

    for i, node in enumerate(inputs):
        print_heap(heap, i)
    # print(heap)
    exit(0)


if __name__ == "__main__":
    main()

