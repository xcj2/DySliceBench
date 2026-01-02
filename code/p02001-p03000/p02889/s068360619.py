#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):

  def __init__(self):
    self.fixed = False
    self.supply = 300
    self.tank = 0
    self.edges = []

  def __repr__(self):
    return str(self)

  def __str__(self):
    return '{}/{}({})'.format(self.supply, self.tank, int(self.fixed))


def main():
  n, m, tank = map(int, input().split())
  nodes = [Node() for _ in range(n)]

  for _ in range(m):
    a, b, c = map(int, input().split())

    nodes[a - 1].edges.append((nodes[b - 1], c))
    nodes[b - 1].edges.append((nodes[a - 1], c))

  queries = [list(map(int, input().split())) for _ in range(int(input()))]
  results = [[None] * len(nodes) for _ in range(len(nodes))]

  for start in range(len(nodes)):
    for node in nodes:
      node.fixed = False
      node.supply = 300
      node.tank = 0

    nodes[start].supply = 0
    nodes[start].tank = tank

    while True:
      targets = [n for n in nodes if not n.fixed ]

      if len(targets) == 0:
        break

      target = min(targets, key=lambda n: (n.supply, -n.tank))
      target.fixed = True

      for n, d in target.edges:
        if n.fixed or d > tank:
          continue

        if d > target.tank:
          new_supply = target.supply + 1
          new_tank = tank - d
        else:
          new_supply = target.supply
          new_tank = target.tank - d

        if (new_supply, -new_tank) < (n.supply, -n.tank):
          n.supply = new_supply
          n.tank = new_tank

    for end in range(len(nodes)):
      results[start][end] = nodes[end].supply

  for start, end in queries:
    if results[start - 1][end - 1] == 300:
      print(-1)
    else:
      print(results[start - 1][end - 1])


if __name__ == '__main__':
  main()
