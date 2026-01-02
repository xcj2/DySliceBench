import sys

sys.setrecursionlimit(2000000000)


class Node:
    def __init__(self, index):
        self.index = index
        self.connected_indices = set()

    def __repr__(self):
        return '{}: {}'.format(self.index, self.connected_indices)


def build_graph(nodes, curr_index, connected_indices, reached_indices):
    # already reached
    if curr_index in connected_indices or curr_index in reached_indices:
        return

    connected_indices |= {curr_index}
    reached_indices |= {curr_index}

    unreached_indices = nodes[curr_index].connected_indices - connected_indices

    for i in unreached_indices:
        build_graph(nodes, i, connected_indices, reached_indices)

    return connected_indices


# if True:
#     line_index = 0
#
#
#     def input():
#         global line_index
#         lines = ['10 8',
#                  '5 3 6 8 7 10 9 1 2 4',
#                  '3 1',
#                  '4 1',
#                  '5 9',
#                  '2 5',
#                  '6 5',
#                  '3 5',
#                  '8 9',
#                  '7 9']
#
#         line = lines[line_index]
#         line_index += 1
#         return line

if __name__ == '__main__':
    N, M = map(int, input().split())
    p = [int(v) - 1 for v in input().split()]

    nodes = [Node(i) for i in range(N)]
    for _ in range(M):
        xy_str = input().split()
        x, y = int(xy_str[0]) - 1, int(xy_str[1]) - 1

        nodes[x].connected_indices |= {y}
        nodes[y].connected_indices |= {x}

    reached_indices = set()
    all_connected_indices = [None] * N
    for i in range(N):
        connected_indices = build_graph(nodes, i, set(), reached_indices)
        if connected_indices is None:
            continue

        for c in connected_indices:
            all_connected_indices[c] = connected_indices

    answer = sum([p[i] in all_connected_indices[i] for i in range(N)])
    print(answer)
    # print(desirable_swaps)
    # print(nodes)
