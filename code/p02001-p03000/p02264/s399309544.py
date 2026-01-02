#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections


class Process(object):

    def __init__(self, name, time):
        self.name = name
        self.time = int(time)


def schedule(processes, quantum):
    queue = collections.deque(processes)
    time = 0
    while len(queue) > 0:
        p = queue.popleft()
        rest_time = p.time - quantum
        if rest_time > 0:
            time += quantum
            queue.append(Process(p.name, rest_time))
        else:
            time += p.time
            print("{name} {time:d}".format(name=p.name, time=time))


def main():
    [n, q] = list(map(int, input().split()))
    processes = [Process(*input().split()) for i in range(n)]
    schedule(processes, q)


if __name__ == "__main__":
    main()