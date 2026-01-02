import math
import collections
import numpy as np


class Edge:
    def __init__(self, dst, color):
        self.dst = dst
        self.color = color

    def __repr__(self):
        return str(self.dst) + ' ' + str(self.color)


def main():
    N = int(input())
    adj_list = [[] for _ in range(N+1)]
    edge_order = []
    for _ in range(N-1):
        a, b = list(map(int, input().split()))
        edge_order.append((a, len(adj_list[a])))
        adj_list[a].append(Edge(b, None))
        adj_list[b].append(Edge(a, None))

    max_deg = 0
    for i in range(1, N+1):
        max_deg = max(max_deg, len(adj_list[i]))
    K = max_deg
    print(K)

    queue = collections.deque()
    queue.append((1, None))
    while queue:
        cur_node, used_color = queue.popleft()
        # print(' ')
        # print('cur_node: ', cur_node)
        # print('used_color: ', used_color)
        # print('adj_list: ', adj_list)

        # color is [0, K-1]
        if used_color is None:
            color = 0
        else:
            color = (used_color + 1) % K
        for edge in adj_list[cur_node]:
            if edge.color is not None:
                pass
            else:
                edge.color = color
                for inv_edge in adj_list[edge.dst]:
                    if inv_edge.dst == cur_node:
                        inv_edge.color = color
                adj_list[edge.dst]
                queue.append((edge.dst, color))
                color = (color + 1) % K
        # print('queue: ', queue)

    for i, j in edge_order:
        print(adj_list[i][j].color + 1)


if __name__ == '__main__':
    main()
