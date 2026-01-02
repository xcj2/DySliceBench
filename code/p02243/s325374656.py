import heapq

class Pair:
    def __init__(self, num=None, wei=None):
        self.num = num
        self.wei = wei # weight
    def __str__(self):
        return str(self.num) + ' ' + str(self.wei)

def createAdjList():
    adjList = []
    for i in range(n):
        innerList = []
        u, k, *v = map(int, input().split())
        for j in range(0, k*2, 2):
            # [weight, num] (not [num, weigt])
            # Comparison of lists in Python is lexicographical -  the first non-equal pair determines the winner of the ordering
            newPair = [v[j+1],v[j]]
            innerList.append(newPair)
        adjList.append(innerList)
    return adjList

#TODO: write dijkstra
def dijkstra():
    d[0] = 0
    pq = []
    pq.append([0,0])
    heapq.heapify(pq)

    while len(pq) > 0:
        # cost が最小の node を選択
        uWei, uNum  = heapq.heappop(pq)

        status[uNum] = VISITED

        # uWei が最小コストでない場合は無視 (wight 更新前に push された、最短ではないルート)
        if d[uNum] < uWei:
            continue

        # u と v をつなぐ edge のうち最小の経路のコストの合計に更新
        for v in adjList[uNum]:
            vNum = v[1]
            vWei = v[0]
            if status[vNum] != VISITED and d[uNum] + vWei < d[vNum]:
                d[vNum] = d[uNum] + vWei
                status[vNum] = VISITING
                heapq.heappush(pq, [d[vNum], vNum])

import sys
# sys.stdin = open('input.txt')

n = int(input())
NOT_VISITED = 0 # WHITE
VISITING = 1 # GRAY
VISITED = 2 # BLACK
INFTY = 10**21

status = [NOT_VISITED] * n
d = [INFTY] * n
p = [-1] * n

adjList = createAdjList()
dijkstra()
for i in range(n):
    print(i, d[i])
