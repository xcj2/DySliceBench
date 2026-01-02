#!/usr/bin/env python3

from heapq import heappop, heappush


x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

class CakeSet:
    def __init__(self, status):
        self.status = status
        self.cost = calc_cost(status)

    def next_list(self):
        ret = []
        if self.status[0] + 1 < x:
            ret.append(CakeSet((self.status[0] + 1, self.status[1], self.status[2])))
        if self.status[1] + 1 < y:
            ret.append(CakeSet((self.status[0], self.status[1] + 1, self.status[2])))
        if self.status[2] + 1 < z:
            ret.append(CakeSet((self.status[0], self.status[1], self.status[2] + 1)))
        return ret

    def __lt__(self, other):
        return self.cost > other.cost

def calc_cost(status):
    return a[status[0]] + b[status[1]] + c[status[2]]

def main():
    memo = set()
    initial = CakeSet((0, 0, 0))
    costs = []
    queue = []
    heappush(queue, initial)
    while len(costs) < k:
        cakeSet = heappop(queue)
        if cakeSet.status in memo:
            continue
        costs.append(cakeSet.cost)
        memo.add(cakeSet.status)
        for next_set in cakeSet.next_list():
            heappush(queue, next_set)
    for cost in costs[:k]:
        print(cost)


if __name__ == '__main__':
    main()
