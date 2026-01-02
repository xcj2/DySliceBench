#!/usr/bin/python

# AtCoder Beginner Contest 075
# D - Axis-Parallel Rectangle

from sys import stdin

def nPointsInRect(y0, y1, points):
  return len([p for p in points if y0 <= p[1] <= y1])

def solve(K, points):
  points.sort()  # sort the points by x-coordinates
  xs = [p[0] for p in points]          # sorted x-coordinates
  ys = sorted([p[1] for p in points])  # sorted y-coordinates
  minArea = (xs[-1] - xs[0]) * (ys[-1] - ys[0])  # the biggest rect
  for i0 in range(len(points)):
    for i1 in range(i0 + K - 1, len(points)):
      for j in range(len(ys)):
        y0 = ys[j]
        for y1 in ys[j + K - 1:]:
          if nPointsInRect(y0, y1, points[i0 : i1 + 1]) >= K:
            area = (xs[i1] - xs[i0]) * (y1 - y0)
            minArea = min(minArea, area)
            break  # no other rects for the same i0, i1, y0 are unnecessary
  return minArea

def splitToInt(line):
  words = line.strip().split()
  return [int(w) for w in words]

N, K = splitToInt(stdin.readline())
points = []
for i in range(N):
  x, y = splitToInt(stdin.readline())
  points.append((x, y))
print(solve(K, points))