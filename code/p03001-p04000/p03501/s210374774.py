#!/usr/bin/python3
# vim: set fileencoding=utf-8:
import sys
input = sys.stdin.readline

"""
H = int(input())
h = [int(ele) for ele in input().split()]
h = [0] + h
"""


def main():
    N, A, B = map(int, input().split())
    print(min(B, N*A))


def bfs(queue):
    global yet, graph
    if len(queue) == 0:
        return
    yet.remove(queue[-1])

    for i, adjacency in enumerate(graph[queue[-1]]):
        if adjacency == 1 and (i in yet) and (i not in queue):  # 隣接かつ未探索であれば、stackにpush
            queue.appendleft(i)
    else:
        queue.pop()
        bfs(queue)


def dfs(stack):
    global yet, graph
    yet.remove(stack[-1])

    for i, adjacency in enumerate(graph[stack[-1]]):
        if adjacency == 1 and i in yet:  # 隣接かつ未探索であれば、stackにpush
            stack.append(i)
            dfs(stack)
    else:
        stack.pop()


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
        if i != n // i:
            divisors.append(n//i)
    return divisors


class Node():

    def __init__(self):
        self.idx = None
        self.left = None
        self.right = None
        self.parent = None
        return

    def pre_order(self):
        global pre_order_str
        pre_order_str += str(self.idx) + " "
        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        global in_order_str

        if self.left:
            self.left.in_order()

        in_order_str += str(self.idx) + " "

        if self.right:
            self.right.in_order()

    def post_order(self):
        global post_order_str
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        post_order_str += str(self.idx) + " "


class HeapHelper():
    """HeapContrler.
    完全二分木を二分ヒープで表現した配列 A に対して、
    HeapHelper.parent(idx) とするとそのノードの親の添字を返す
    存在しない場合は Falseを返す

    Returns:
        [type] -- [description]
    """

    def __init__(self):
        return

    @staticmethod
    def parent(i):
        if i == 1:
            return False

        return int(i/2)

    @staticmethod
    def left(i):
        l_idx = 2*i
        if H < l_idx:
            return False

        return l_idx

    @staticmethod
    def right(i):
        r_idx = 2*i + 1
        if H < r_idx:
            return False

        return r_idx


if __name__ == "__main__":
    main()
