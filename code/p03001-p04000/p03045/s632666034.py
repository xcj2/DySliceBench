# -*- coding: utf-8 -*-

def readInts():
  return [int(s) for s in input().split(" ")]

def root(groups, n):
  i = n
  while groups[i] != i:
    i = groups[i]
  groups[n] = i
  return i

def union(groups, x, y):
  rx = root(groups, x)
  ry = root(groups, y)
  if rx != ry:
    groups[ry] = rx

def main():
  N, M = readInts()
  groups = [i for i in range(N)]

  for i in range(M):
    X, Y, Z = readInts()
    union(groups, X-1, Y-1)

  knowns = set()
  for n in range(N):
    knowns.add(root(groups, n))
  print(len(knowns))

if __name__ == "__main__":
  main()
