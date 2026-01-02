#!/usr/bin/env python3

from collections import defaultdict
import sys

sys.setrecursionlimit(2000)


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for u, v in connections:
            self.add(u, v)

    def add(self, u, v):
        """ Add connection between node u and node v """

        self._graph[u].add(v)
        if not self._directed:
            self._graph[v].add(u)

    def remove(self, v):
        """ Remove all references to node v """

        for _, cxns in self._graph.items():
            try:
                cxns.remove(v)
            except KeyError:
                pass
        try:
            del self._graph[v]
        except KeyError:
            pass

    def get_adj(self, v):
        """ Get adjacency list of node v """
        return self._graph[v]

    def is_connected(self, u, v):
        """ Is node u directly connected to node v """

        return u in self._graph and v in self._graph[u]

    def find_path(self, src, dst, path=[]):
        """ Find any path from src node to dst node (may not be shortest) """

        path = path + [src]
        if src == dst:
            return path
        if src not in self._graph:
            return None
        for src_next in self._graph[src]:
            if src_next not in path:
                new_path = self.find_path(src_next, dst, path)
                if new_path:
                    return new_path
        return None

    def find_all_paths(self, src, dst, path=[]):
        """ Find all paths from src node to dst node """
        path = path + [src]
        if src == dst:
            return path
        if src not in self._graph:
            return None
        paths = []
        for src_next in self._graph[src]:
            if src_next not in path:
                new_path = self.find_all_paths(src_next, dst, path)
                if new_path:
                    paths.append(new_path)
        if len(paths) > 0:
            return paths
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def adj_list(c, i, j):
    top, bot = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    top_left, top_right = [i - 1, j - 1], [i - 1, j + 1]
    bot_left, bot_right = [i + 1, j - 1], [i + 1, j + 1]
    if i == 0:
        if j == 0:
            return [right, bot, bot_right]
        elif j == w - 1:
            return [left, bot, bot_left]
        else:
            return [left, right, bot_left, bot, bot_right]
    elif i == h - 1:
        if j == 0:
            return [top, right, top_right]
        elif j == w - 1:
            return [top, left, top_left]
        else:
            return [left, right, top, top_left, top_right]
    else:
        if j == 0:
            return [top, right, top_right, bot, bot_right]
        elif j == w - 1:
            return [top, left, top_left, bot, bot_left]
        else:
            return [top, bot, left, right, top_left, top_right, bot_left, bot_right]


def is_reachable(c, i, j, i_adj, j_adj):
    if c[i][j] == 1 and c[i_adj][j_adj] == 1:
        return True
    return False


def dfs(g, v):
    seen[v] = True
    for v_next in g.get_adj(v):
        if not seen.get(v_next):
            dfs(g, v_next)


#-----
# 1 <= w, h <= 50
# c_{i, j} = 0, 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    c = []
    if w == 1 and h == 1:
        c = int(input())
        if c == 1:
            print(1)
        else:
            print(0)
    else:
        for _ in range(h):
            line = list(map(int, input().split()))
            c.append(line)
        # print(h, w, c)

        g = Graph([])
        for i in range(0, h):
            for j in range(w):
                # print(f"(i, j): ({i}, {j})")
                u = (i * w) + j
                is_connected = False
                for adj in adj_list(c, i, j):
                    i_adj, j_adj = adj[0], adj[1]
                    # print(f"(i_adj, j_adj): ({i_adj}, {j_adj})")
                    if is_reachable(c, i, j, i_adj, j_adj):
                        is_connected = True
                        v = i_adj * w + j_adj
                        g.add(u, v)
                if c[i][j] == 1 and not is_connected:
                    g.add(u, u)
        # print(g)

        keys = [v for v in range(h * w)]
        values = [False for _ in range(h * w)]
        seen = dict(zip(keys, values))

        num_connected_components = 0
        for v in range(h * w):
            if not seen[v]:
                if len(g.get_adj(v)) > 0:
                    num_connected_components += 1
                dfs(g, v)

        print(num_connected_components)

