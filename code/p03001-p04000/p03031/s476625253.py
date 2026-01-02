#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import copy


class Node(object):

  def __init__(self, n, m):
    self.lamps = [[0] * n for _ in range(m)]
    self.status = [[0, 0] for _ in range(m)]
    self.index = 0

  def create_children(self):
    children = []

    child0 = copy.deepcopy(self)
    child1 = copy.deepcopy(self)

    for i in range(len(self.status)):
      child0.status[i][0] -= child0.lamps[i][self.index]
      child1.status[i][0] -= child1.lamps[i][self.index]
      child1.status[i][1] += child1.lamps[i][self.index]

    child0.index += 1
    child1.index += 1

    if child0.is_valid():
      children.append(child0)

    if child1.is_valid():
      children.append(child1)

    return children

  def is_valid(self):
    for r, v in self.status:
      if r == 0 and v % 2 == 1:
        return False

    return True


def main():
  n, m = map(int, input().split())
  root = Node(n, m)

  for i in range(m):
    v = list(map(int, input().split()))[1:]

    for j in v:
      root.lamps[i][j - 1] = 1

    root.status[i][0] = len(v)

  for i, v in enumerate(map(int, input().split())):
    root.status[i][1] = v

  stack = collections.deque()
  stack.append(root)
  count = 0

  while len(stack) != 0:
    node = stack.pop()

    children = node.create_children()

    for child in children:
      if child.index == n:
        count += 1
      else:
        stack.append(child)

  print(count)


if __name__ == '__main__':
  main()

