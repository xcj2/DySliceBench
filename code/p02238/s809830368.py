# coding: utf-8
import itertools
import math
import bisect

class Node:
    def __init__(self, id, next, rest):
        self.id = id
        self.before = None
        self.next = next
        self.rest = rest
        self.d = None
        self.f = None

    def update_next(self):
        self.next = first(self.rest)
        self.rest = rest(self.rest)


N = int(input())
graph = []
for _ in range(N):
    l = list(map(int, input().split(" ")))
    id = l[0]
    if l[1] != 0:
        next = l[2]
    else:
        next = None
    if l[1] >= 2:
        rest = l[3:]
    else:
        rest = []
    graph.append(Node(l[0], next, rest))

def first(l):
    if l==None:
        return None
    if len(l) == 0:
        return None
    else:
        return l[0]

def rest(l):
    if l == None:
        return None
    if len(l) >= 2:
        return l[1:]
    else:
        return None

def dfs(graph):
    stack = [graph[0]]
    stack[-1].d = 1
    tansakuzumi = [1]
    mitansaku = list(range(1, len(graph)+1))
    res_graph = []
    t = 2
    while len(stack) != 0:
        tansakuzumi.append(stack[-1].id)
        if stack[-1].id in mitansaku:
            mitansaku.remove(stack[-1].id)
        if stack[-1].next == None:
            stack[-1].f = t
            res_graph.append(stack.pop())
            t += 1
        elif stack[-1].next in tansakuzumi:
            stack[-1].update_next()
        else:
            stack.append(graph[stack[-1].next-1])
            stack[-2].update_next()
            stack[-1].d = t
            t += 1
        if len(stack) == 0 and len(mitansaku) >= 1:
            stack.append(graph[mitansaku[0]-1])
            stack[-1].d = t
            t += 1
    return res_graph




res_graph = dfs(graph)

res_graph.sort(key=lambda x: x.id)

for n in res_graph:
    print("{} {} {}".format(n.id, n.d, n.f))

