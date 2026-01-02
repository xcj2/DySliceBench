#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array
import collections


class Solver(object):

    deltas = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

    def __init__(self, gems, initial_point=(10, 10)):
        self.gems = gems
        self.current_point = initial_point
        self.visited = collections.defaultdict(bool)

    def move(self, direction, distance):
        (x0, y0) = self.current_point
        (dx, dy) = self.deltas[direction]
        for i in range(1, distance + 1):
            (x, y) = (x0 + i * dx, y0 + i * dy)
            self.current_point = (x, y)
            self.visited[(x, y)] = True

    def moves(self, commands):
        for direction, distance in commands:
            self.move(direction, distance)

    def judge(self):
        for gem in self.gems:
            if not self.visited[gem]:
                return False
        else:
            return True


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        gems = [tuple(map(int, input().split())) for _ in range(n)]
        m = int(input())
        commands = []
        for _ in range(m):
            direction, distance = input().split()
            distance = int(distance)
            commands.append((direction, distance))
        solver = Solver(gems)
        solver.moves(commands)
        if solver.judge():
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()