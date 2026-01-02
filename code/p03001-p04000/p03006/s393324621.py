# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

def cost(N, points, pointToIndex, p, q):
  s = 0

  visited = [False for _ in range(N)]
  for i in range(N):
    if visited[i]: continue

    s += 1
    visited[i] = True

    k = 1
    while (points[i][0] + p * k <= points[-1][0]) and (points[i][1] + q * k <= points[-1][1] or points[i][1] + q * k >= points[-1][1]):
      np = (points[i][0] + p * k, points[i][1] + q * k)
      if np in pointToIndex and not visited[pointToIndex[np]]:
        visited[pointToIndex[np]] = True
        k += 1
      else:
        break

  return s

def main():
  N = readInts()[0]
  points = [tuple(readInts()) for _ in range(N)]
  points.sort()

  ans = N

  pointToIndex = {}
  for i, point in enumerate(points):
    pointToIndex[point] = i

  for i in range(N-1):
    for j in range(i+1, N):
      p = points[j][0] - points[i][0]
      q = points[j][1] - points[i][1]
      ans = min(ans, cost(N, points, pointToIndex, p, q))

  print(ans)

if __name__ == "__main__":
  main()
