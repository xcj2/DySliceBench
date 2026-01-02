#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


class Node(object):

  def __init__(self):
    self.edges = []


class Edge(object):

  def __init__(self):
    self.color = -1


def main():
  nodes = [Node() for _ in range(int(input()))]
  edges = [Edge() for _ in range(len(nodes) - 1)]

  for i in range(len(nodes) - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    nodes[a].edges.append((edges[i], nodes[b]))
    nodes[b].edges.append((edges[i], nodes[a]))

  queue = collections.deque()
  node = nodes[0]

  for i in range(len(node.edges)):
    node.edges[i][0].color = i
    queue.append(node.edges[i][1])

  max_color = len(node.edges) - 1

  while len(queue) != 0:
    node = queue.popleft()
    exist = -1
    index = 0

    for i in range(len(node.edges)):
      if node.edges[i][0].color != -1:
        exist = node.edges[i][0].color
        break

    for i in range(len(node.edges)):
      if index == exist:
        index += 1

      if node.edges[i][0].color != -1:
        continue

      node.edges[i][0].color = index
      index += 1
      queue.append(node.edges[i][1])

    max_color = max(len(node.edges) - 1, max_color)

  print(max_color + 1)
  for e in edges:
    print(e.color + 1)


if __name__ == '__main__':
  main()
