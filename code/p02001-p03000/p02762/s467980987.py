import unittest
import collections


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(
                4,
                [
                    [2, 1],
                    [1, 3],
                    [3, 2],
                    [3, 4],
                ],
                [
                    [4, 1]
                ]
            ),
            [0, 1, 0, 1]
        )

    def test_2(self):
        self.assertEqual(
            think(
                5,
                [
                    [1, 2],
                    [1, 3],
                    [1, 4],
                    [1, 5],
                    [3, 2],
                    [2, 4],
                    [2, 5],
                    [4, 3],
                    [5, 3],
                    [4, 5],
                ],
                [
                ]
            ),
            [0, 0, 0, 0, 0]
        )

    def test_3(self):
        self.assertEqual(
            think(
                10,
                [
                    [10, 1],
                    [6, 7],
                    [8, 2],
                    [2, 5],
                    [8, 4],
                    [7, 3],
                    [10, 9],
                    [6, 4],
                    [5, 8],
                ],
                [
                    [2, 6],
                    [7, 5],
                    [3, 1],
                ]
            ),
            [1, 3, 5, 4, 3, 3, 3, 3, 1, 0]
        )


def solve():
    n, list_of_a_and_b, list_of_c_and_d = read()
    result = think(n, list_of_a_and_b, list_of_c_and_d)
    write(result)


def read():
    n, m, k = read_int(3)
    list_of_a_and_b = []
    for _ in range(m):
        a, b = read_int(2)
        list_of_a_and_b.append([a, b])
    list_of_c_and_d = []
    for _ in range(k):
        c, d = read_int(2)
        list_of_c_and_d.append([c, d])
    return n, list_of_a_and_b, list_of_c_and_d


def read_int(n):
    return read_type(int, n, sep=' ')


def read_float(n):
    return read_type(float, n, sep=' ')


def read_type(t, n, sep):
    return list(map(lambda x: t(x), read_line().split(sep)))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(n, list_of_a_and_b, list_of_c_and_d):
    adjacency_list_of_friend = make_adjacency_list_from(n, list_of_a_and_b)
    adjacency_list_of_block = make_adjacency_list_from(n, list_of_c_and_d)
    list_of_connected_graph = collect_connected_graph_from(n, adjacency_list_of_friend)
    candidate_of_friends = [0] * n
    for connected_graph in list_of_connected_graph:
        for vertex in connected_graph:
            index = vertex - 1
            candidate_of_friends[index] = len(connected_graph)
            candidate_of_friends[index] -= len(adjacency_list_of_friend[vertex])
            for blocked in adjacency_list_of_block[vertex]:
                if blocked in connected_graph:
                    candidate_of_friends[index] -= 1
            candidate_of_friends[index] -= 1
    return candidate_of_friends


def write(result):
    print(' '.join(map(str, result)))


def make_adjacency_list_from(n, list_of_pair):
    adjacency_list = {}
    for i in range(1, n + 1):
        adjacency_list[i] = []
    for left, right in list_of_pair:
        adjacency_list[left].append(right)
        adjacency_list[right].append(left)
    return adjacency_list


def collect_connected_graph_from(n, adjacency_list):
    visited = [False for _ in range(n + 1)]
    list_of_connected_graph = []
    for vertex in range(1, len(visited)):
        if visited[vertex]:
            continue
        connected_graph = set([vertex])
        queue = collections.deque([vertex])
        while queue:
            data = queue.popleft()
            if visited[data]:
                continue
            visited[data] = True
            connected_graph.add(data)
            for next_data in adjacency_list[data]:
                queue.append(next_data)
        list_of_connected_graph.append(connected_graph)
    return list_of_connected_graph


if __name__ == '__main__':
    # unittest.main()
    solve()