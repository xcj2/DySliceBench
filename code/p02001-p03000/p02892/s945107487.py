#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):

  def __init__(self, idx):
    self.idx = idx
    self.edges = []
    self.depth = -1

  def __str__(self):
    return '{}: -> {}'.format(self.idx, ','.join(str(e.idx) for e in self.edges))


def search(nodes):
  new_nodes = set()

  for node in nodes:
    for edge in node.edges:
      if edge.depth == -1:
        edge.depth = node.depth + 1
        new_nodes.add(edge)
      elif abs(edge.depth - node.depth) != 1:
        return False

  if len(new_nodes) == 0:
    return True

  return search(new_nodes)


def main():
  nodes = [Node(i) for i in range(int(input()))]
  value = 0

  for i in range(len(nodes)):
    for j, v in enumerate(map(int, input().strip())):
      if v == 1:
        nodes[i].edges.append(nodes[j])

  for i in range(len(nodes)):
    for node in nodes:
      node.depth = -1

    start = nodes[i]
    start.depth = 1

    if not search([start]):
      print(-1)
      return

    for node in nodes:
      value = max(node.depth, value)

  print(value)


if __name__ == '__main__':
  main()
