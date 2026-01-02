S = input().split(" ")
N = int(S[0])
M = int(S[1])
ARR = []
for i in range(M):
    ARR.append([int(s) for s in input().split(" ")])



def prepare(n, m, arr):
    nodes = [[] for i in range(n)]
    nodeStates = [0 for i in range(n)]
    for i in range(m):
        nodeFrom = arr[i][0] - 1
        nodeTo = arr[i][1] - 1
        nodes[nodeFrom].append(nodeTo)
        nodes[nodeTo].append(nodeFrom)

    return nodes, nodeStates


nodes, nodeStates = prepare(N, M, ARR)


def dfs(currentNodeIndex, arr, nodeStates):
    if nodeStates[currentNodeIndex] == 0:
        nodeStates[currentNodeIndex] = 1

    childNodes = arr[currentNodeIndex]
    for childNodeIndex in childNodes:
        if nodeStates[childNodeIndex] == 0:
            dfs(childNodeIndex, arr, nodeStates)

    return nodeStates


# dfs(0, nodes)


def calculate(n, m, arr):
    arr = list(arr)
    result = 0
    for ar in arr:
        brr = arr.copy()
        brr.remove(ar)
        nodes, nodeStates = prepare(n, m-1, brr)
        nodeStatesResult = dfs(0,nodes,nodeStates)
        if sum(nodeStatesResult) != n:
            result = result + 1
    print(result)


calculate(N,M,ARR)
