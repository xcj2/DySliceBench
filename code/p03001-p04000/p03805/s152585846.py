n, m = map(int, input().split())

graphs = list([list(map(int, input().split())) for x in range(m)])

def search_indecies(num, remainGraph, path):
    indecies = []
    for i, currentNode in enumerate(remainGraph):
        if currentNode[0] == num or currentNode[1] == num:
            others = get_other_num(currentNode, num)
            if all([x[0] != others and x[1] != others for x in path]):
                indecies.append(i)
    return indecies



def search_iterative(currentGraph, currentNodeNum, currentIndex, path):
    prev = currentNodeNum

    currentNode = currentGraph.pop(currentIndex)
    path.append(currentNode)
    if len(path) == n - 1:
        return [path]
    nextNum = get_other_num(currentNode, prev)

    nextCandidateIndecies = search_indecies(nextNum, currentGraph, path)

    pathList = []
    for nextIndex in nextCandidateIndecies:
        c = search_iterative(currentGraph[:], nextNum, nextIndex, path[:])
        pathList += c

    return pathList

def get_other_num(currentNode, prev):
    return currentNode[0] if currentNode[1] == prev else currentNode[1]


startIndecies = search_indecies(1, graphs, [])

resuts = []
for startIndex in startIndecies:
    path = []
    resuts += search_iterative(graphs[:], 1, startIndex, path)

allPaths = [r for r in resuts if len(r) > 0]
print(len(allPaths))