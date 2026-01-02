#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
import math


def inputIntList():
  return [int(s) for s in input().split()]


def inputInt():
  return int(input())


def main():
  H, W = inputIntList()
  S = [[s for s in input()] for _ in range(H)]

  ans = 0
  for si in range(H):
    for sj in range(W):
      if S[si][sj] == '#':
        continue

      dist = [[-1 for _ in range(W)] for _ in range(H)]
      q = deque()

      start = (si, sj)
      if dist[si][sj] == -1:
        dist[si][sj] = 0
        q.append(start)

      while q:
        qi, qj = q.popleft()
        for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
          ni = qi + di
          nj = qj + dj
          if ni < 0 or ni >= H:
            continue
          if nj < 0 or nj >= W:
            continue
          if S[ni][nj] == '#':
            continue
          if dist[ni][nj] == -1:
            dist[ni][nj] = dist[qi][qj]+1
            q.append((ni, nj))
            ans = max(ans, dist[ni][nj])
  return ans


if __name__ == "__main__":
  print(main())
