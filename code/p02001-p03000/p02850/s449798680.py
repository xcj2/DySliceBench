# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10000000)

def readInts():
  return [int(s) for s in input().split(" ")]

def next_color(c, exclude):
  if c == exclude:
    return c + 1
  else:
    return c

def traverse(N, edges, k, ans, v, exclude = 0):
  c = next_color(1, exclude)
  for (b, i) in edges[v]:
    ans[i] = c
    traverse(N, edges, k, ans, b, c)
    c = next_color(c + 1, exclude)

def main():
  N = readInts()[0]
  edges = [[] for _ in range(N)]
  counts = [0 for _ in range(N)]
  for i in range(N-1):
    a, b = readInts()
    a -= 1
    b -= 1
    edges[a].append((b, i))
    counts[a] += 1
    counts[b] += 1

  k = max(counts)
  ans = [0 for _ in range(N-1)]
  traverse(N, edges, k, ans, 0)

  print(k)
  for i in range(N-1):
    print(ans[i])

if __name__ == "__main__":
  main()
