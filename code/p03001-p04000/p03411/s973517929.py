#  --*-coding:utf-8-*--

def fulkerson(graph, src, sink):
    n = len(graph)

    matrix = [[0]*n for i in range(n)]
    bothDirGraph = [[] for i in range(n)]

    for nodeId, edges in enumerate(graph):
        for nodeId2, flowLimit in edges:
            matrix[nodeId][nodeId2] = flowLimit
            bothDirGraph[nodeId].append(nodeId2)
            bothDirGraph[nodeId2].append(nodeId)

    while True:
        path = findPath(bothDirGraph, matrix, src, sink)

        if path == None:
            break

        v = min(matrix[path[i]][path[i+1]] 
                for i in range(len(path)-1))

        for i in range(len(path)-1):
            node1 = path[i]
            node2 = path[i+1]
            
            matrix[node1][node2] -= v
            matrix[node2][node1] += v

    return (sum(c for _, c in graph[src]) - 
            sum(c for c in matrix[src]))


def findPath(bothDirGraph, matrix, src, sink):
    prevs = [None]*len(matrix)
    q = set([src])
    prevs[src] = src

    while len(q) > 0:
        node = q.pop()

        for nextNode in bothDirGraph[node]:
            if prevs[nextNode] == None and matrix[node][nextNode] > 0:
                prevs[nextNode] = node
                
                if nextNode == sink:
                    path = []
                    pathNode = sink

                    while pathNode != src:
                        path.append(pathNode)
                        pathNode = prevs[pathNode]

                    path.append(src)
                    return list(reversed(path))

                q.add(nextNode)

    return None
                    

def main():
    N = int(input())
    graph = [[] for i in range(2*N+2)]
    
    for i in range(N):
        graph[0].append(((i+1)*2, 1))
        graph[(i+1)*2+1].append((1, 1))

    p1s = [tuple(map(int, input().split())) for i in range(N)]
    p2s = [tuple(map(int, input().split())) for i in range(N)]

    for i1, p1 in enumerate(p1s):
        for i2, p2 in enumerate(p2s):
            if p1[0] < p2[0] and p1[1] < p2[1]:
                graph[(i1+1)*2].append(((i2+1)*2+1, 1))

    print(fulkerson(graph, 0, 1))


if __name__ == '__main__':
    main()
