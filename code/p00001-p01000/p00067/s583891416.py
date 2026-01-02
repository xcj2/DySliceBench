# -*- coding: utf-8 -*-

import sys
import os

def solve(island):
    visited = []
    for lst in island:
        visit_row = []
        for c in lst:
            if c == '1':
                visit_row.append(False)
            else:
                visit_row.append(True)
        visited.append(visit_row)

    def paintable(x, y):
        if 0 <= x < 12 and 0 <= y < 12 and not visited[x][y]:
            return True
        else:
            return False

    def paint(x, y, number):
        visited[x][y] = True
        island[x][y] = number
        if paintable(x-1, y):
            paint(x-1, y, number)

        if paintable(x+1, y):
            paint(x+1, y, number)

        if paintable(x, y-1):
            paint(x, y-1, number)

        if paintable(x, y+1):
            paint(x, y+1, number)

    paint_id = 2

    for i in range(12):
        for j in range(12):
            if paintable(i, j):
                paint(i, j, paint_id)
                paint_id += 1

    line = []
    for lst in island:
        line += lst

    line = set(line)
    if '0' in lst:
        line.remove('0')

    print(len(line))

for s in sys.stdin:
    s = s.strip()
    if s != '':
        island = [list(s)]
        for i in range(11):
            s = input().strip()
            island.append(list(s))
        solve(island)
    else:
        island = []
        pass