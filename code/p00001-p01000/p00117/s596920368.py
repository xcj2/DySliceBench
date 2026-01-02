class Graph():

    from collections import namedtuple
    __Pair = namedtuple("Pair", "cost point")

    def __init__(self, townCount):
        self.__townCount = townCount
        self.__adjacencyList = [[] for _ in range(townCount)]

    def GetPath(self, beginPoint, endPoint, cost):
        item = self.__Pair(cost, endPoint)
        self.__adjacencyList[beginPoint].append(item)

    def Dijkstra(self, beginPoint):

        from sys import maxsize as MaxValue
        from queue import PriorityQueue
        stateTable = {"NotVisited": 0, "Stay": 1, "Visited": 2}

        # 初期化
        pq = PriorityQueue()
        costTable = [MaxValue for _ in range(self.__townCount)]
        visitState = [stateTable["NotVisited"]
                      for _ in range(self.__townCount)]

        # 処理
        costTable[beginPoint] = 0
        pq.put_nowait(self.__Pair(0, beginPoint))

        while not pq.empty():

            minItem = pq.get_nowait()
            minPoint, minCost = minItem.point, minItem.cost

            visitState[minPoint] = stateTable["Visited"]

            if minCost <= costTable[minPoint]:

                for cost, point in self.__adjacencyList[minPoint]:
                    if visitState[point] != stateTable["Visited"]:

                        if costTable[minPoint] + cost < costTable[point]:
                            costTable[point] = costTable[minPoint] + cost
                            visitState[point] = stateTable["Stay"]
                            pq.put_nowait(self.__Pair(costTable[point], point))

        return costTable


# main process
townCount = int(input())
wayCount = int(input())

graph = Graph(townCount)

for lp in range(wayCount):
    begin, end, cost1, cost2 = [int(item) for item in input().split(",")]
    begin -= 1
    end -= 1
    graph.GetPath(begin, end, cost1)
    graph.GetPath(end, begin, cost2)


beginPoint, endPoint, budget, pillarCost = [
    int(item) for item in input().split(",")]

beginPoint -= 1
endPoint -= 1

leaveCost = graph.Dijkstra(beginPoint)
returnCost = graph.Dijkstra(endPoint)

result = budget - pillarCost - leaveCost[endPoint] - returnCost[beginPoint]

print(result)

