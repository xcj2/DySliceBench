# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_C

???????§????????????????II
"""
from enum import Enum
from heapq import heappush, heappop, heapify
import itertools


class Priority_queue():
    # https://docs.python.jp/3/library/heapq.html
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def top_task(self):
        return self.pq[0][-1]

    def get_length(self):
        return len(self.pq)

    def is_empty(self):
        return self.get_length()==0


class Sssp(object):
    """ single source shortest path """
    INFINITY = 999999999
    class Status(Enum):
        """ ?????????????¨??????¶??? """
        white = 1  # ????¨????
        gray = 2  # ?¨???????
        black = 3  #?¨???????

    def __init__(self, data):
        num_of_nodes = len(data)
        self.color = [Sssp.Status.white] * num_of_nodes  # ????????????????¨??????¶???
        self.d = [Sssp.INFINITY] * num_of_nodes  # ?§???????????????????
        self.p = [-1] * num_of_nodes  # ????????????????????????????¨?????????????????????????
        self.adj = [[] for _ in range(num_of_nodes)]
        self.make_adj(data)


    def make_adj(self, data):
        # ??£??\??????????????????
        for d in data:
            my_id = d[0]
            d = d[2:]
            while len(d) > 1:
                to_node, cost = d[0], d[1]
                self.adj[my_id].insert(0, (to_node, cost))
                d = d[2:]


    def dijkstra(self, start):
        self.d[start] = 0
        pq = Priority_queue()
        pq.add_task((0, 0), 0)

        while not pq.is_empty():
            cost, u = pq.pop_task()
            self.color[u] = Sssp.Status.black
            if self.d[u] < cost:
                continue

            for v, cost in self.adj[u]:
                if self.color[v] == Sssp.Status.black:
                    continue
                if self.d[v] > self.d[u] + cost:
                    self.d[v] = self.d[u] + cost
                    pq.add_task((self.d[v], v), self.d[v])
                    self.color[v] = Sssp.Status.gray


if __name__ == '__main__':
    # ??????????????\???
    num = int(input())
    data = []
    for i in range(num):
        data.append(list(map(int, input().split(' '))))

    # ???????????¢?´¢
    s = Sssp(data)
    s.dijkstra(0)

    # ???????????¨???
    for i in range(num):
        print('{0} {1}'.format(i, s.d[i]))