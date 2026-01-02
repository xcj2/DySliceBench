#!/usr/bin/env python3
import collections as cl
import sys
import copy


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


class Maze:
    def __init__(self, base_map, H, W):
        self.H = H
        self.W = W
        self.maze = base_map

        reachable = []
        for i in range(self.H):
            for j in range(self.W):
                reachable.append([i, j])

        self.reachable = reachable

    def solve(self):
        ans = 0
        for start in self.reachable:
            max_cost = self.calc_cost(start)
            ans = max(ans, max_cost)

        print(ans)

    def isNotReachable(self, i, j):
        return i < 0 or i >= self.H or j < 0 or j >= self.W or self.maze[i][j] == -1

    def calc_cost(self, start):
        costs = copy.deepcopy(self.maze)
        deque = cl.deque([])
        deque.append(start)
        ways = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[False for j in range(self.W)] for i in range(self.H)]
        visited[start[0]][start[1]] = True

        while len(deque) > 0:
            cur_point = deque.popleft()
            i, j = cur_point[0], cur_point[1]
            for way in ways:
                next_i = i + way[0]
                next_j = j + way[1]
                if self.isNotReachable(next_i, next_j) or visited[next_i][next_j]:
                    continue
                visited[next_i][next_j] = True
                costs[next_i][next_j] = costs[i][j] + 1
                deque.append([next_i, next_j])
        max_cost = 0
        for row in costs:
            max_cost = max(max_cost, *row)
        return max_cost


def main():
    H, W = MI()
    base_map = []
    for _ in range(H):
        row = input()
        row_in_num = []
        for j in range(len(row)):
            if row[j] == ".":
                row_in_num.append(0)
            else:
                row_in_num.append(-1)

        base_map.append(row_in_num)

    maze = Maze(base_map, H, W)
    maze.solve()


main()
