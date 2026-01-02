from collections import deque

S = input().split(" ")
N = int(S[0])
M = int(S[1])
ARR = []

for i in range(M):
    ARR.append([int(s) for s in input().split(" ")])

def prepare(n, m, arr):
    nodes = [[] for i in range(n)]
    nodeStates = [0 for i in range(n)]

    for ar in arr:
        nodeFrom = ar[0] - 1
        nodeTo = ar[1] - 1
        nodes[nodeFrom].append(nodeTo)
        nodes[nodeTo].append(nodeFrom)

    return nodes, nodeStates


def bfs(startNodeIndex, arr, nodeStates):
    q = deque()

    q.append(startNodeIndex)
    nodeStates[startNodeIndex] = 1

    while q.__len__() > 0:
        nodeIndex = q.popleft()
        childNodes = arr[nodeIndex]
        for childNodeIndex in childNodes:
            if nodeStates[childNodeIndex] == 0:
                q.append(childNodeIndex)
                nodeStates[childNodeIndex] = 1

    return nodeStates


def calculate(n, m, arr):
    arr = list(arr)

    result = 0

    for ar in arr:
        brr = arr.copy()
        brr.remove(ar)

        nodes, nodeStates = prepare(n, m-1, brr)
        nodeStates = bfs(0, nodes, nodeStates)

        if sum(nodeStates) != n:
            result = result + 1

    print(result)



calculate(N, M, ARR)
