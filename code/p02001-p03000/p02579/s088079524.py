#!/usr/bin/env python3
import collections as cl
import sys
MAX_INT = -100


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


class Maze():
    def __init__(self, maze, start, goal, h, w):
        self.maze = maze
        self.h = h
        self.w = w
        self.start = start
        self.goal = goal

    def clastering(self):
        group = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] != -1:
                    continue
                self.fill([i, j], group)
                group += 1
        self.num_group = group

    def fill(self, point, group):
        self.maze[point[0]][point[1]] = group
        deque = cl.deque([point])
        ways = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        while len(deque) > 0:
            cur = deque.popleft()

            for way in ways:
                next_i = cur[0] + way[0]
                next_j = cur[1] + way[1]
                if self.isReachable(next_i, next_j) and self.maze[next_i][next_j] != group:
                    self.maze[next_i][next_j] = group
                    deque.append([next_i, next_j])

    def isReachable(self, i, j):
        return 0 <= i < self.h and 0 <= j < self.w and self.maze[i][j] != MAX_INT

    def solve(self):
        self.clastering()

        connected = [[]for i in range(self.num_group)]

        for i in range(self.h):
            for j in range(self.w):
                if not self.isReachable(i, j):
                    continue

                for i_plus in [-2, -1, 0, 1, 2]:
                    for j_plus in [-2, -1, 0, 1, 2]:
                        next_i = i + i_plus
                        next_j = j + j_plus
                        if self.isReachable(next_i, next_j):
                            next_group = self.maze[next_i][next_j]
                            cur_group = self.maze[i][j]
                            if next_group != cur_group:
                                connected[cur_group
                                          ].append(next_group)

        for g in range(len(connected)):
            connected[g] = list(set(connected[g]))

        start_group = self.maze[self.start[0] - 1][self.start[1]-1]
        goal_group = self.maze[self.goal[0]-1][self.goal[1] - 1]

        if start_group == goal_group:
            print(0)
            return

        if len(connected[start_group]) == 0 or len(connected[goal_group]) == 0:
            print(-1)
            return

        costs = [10**19] * len(connected)

        costs[start_group] = 0
        deque = cl.deque([connected[start_group]])
        cost = 1
        while len(deque) > 0:
            cur = deque.popleft()
            if len(cur) == 0:
                break
            next_g = []
            for group in cur:
                if costs[group] > cost:
                    costs[group] = cost
                    next_g.extend(connected[group])

            cost += 1
            deque.append(next_g)

        print(costs[goal_group])


def main():
    h, w = MI()
    start = LI()
    goal = LI()
    maze = [[MAX_INT for i in range(w)] for j in range(h)]

    for i in range(h):
        row = input()
        for j in range(len(row)):
            if row[j] == "#":
                continue
            maze[i][j] = -1

    solver = Maze(maze, start, goal, h, w)
    solver.solve()


main()
