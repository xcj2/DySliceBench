# coding: utf-8

from queue import Queue

N = int(input())
graph = [None]
for _ in range(N):
    graph.append(list(map(int, input().split(" ")))[1:])

class BFSSolver:

    def __init__(self, graph):
        self.graph = graph
        self.queue = Queue()
        self.queue.put(1)
        self.before_id = 1
        self.already_searched = [1]
        self.res = [0]
        for _ in range(N):
            self.res.append(-1)
        self.res[1] = 0
        self.turn = 0

    def next_turn(self):
        now_id = self.queue.get()
        before_id = now_id
        neighbors = self.graph[now_id][1:]
        for i in neighbors:
            if i not in self.already_searched:
                self.turn = self.res[before_id] + 1
                self.already_searched.append(i)
                self.res[i] = self.turn
                self.queue.put(i)

    def solve(self):
        while not self.queue.empty():
            self.next_turn()

        for id, i in enumerate(self.res[1:]):
            print("{} {}".format(id+1, i))

s = BFSSolver(graph)
s.solve()

