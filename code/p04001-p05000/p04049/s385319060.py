# tree diameter if (currDia <= k) true else shorten() while (dia >= k) O(n) dia readjust 
# multiple pairs . centroid of tree --> on largest path find centroid --> maintain a heap ?

from collections import deque

def main():

    n, d = map(int, input().split())

    adj = [[] for i in range(n)]

    edges = []

    for i in range(n-1):

        a, b = map(int, input().split())

        adj[a-1].append(b-1)

        adj[b-1].append(a-1)

        edges.append((a-1, b-1))


    ans = 1000000

    if (d % 2 == 0):
        for i in range(n):
            ans = min(ans, compute(adj, i, d))
    else:
        for i in range(n-1):
            ans = min(ans, computeEdges(adj, edges[i], d-1))

    print(ans)

def compute(adj, u, dia):

    vis = [False]*len(adj)

    dis = [0]*len(adj)

    q = deque()

    q.append(u)
    vis[u] = True

    while (len(q) > 0):

        elem = q.popleft()

        for v in adj[elem]:

            if (vis[v] == False):
                q.append(v)

                vis[v] = True

                dis[v] = dis[elem] + 1

    count = 0

    for a in dis:

        if (a > dia/2):
            count += 1

    return count


def computeEdges(adj, edge, dia):

    vis = [False]*len(adj)

    dis = [0]*len(adj)

    q = deque()

    q.append(edge[0])
    q.append(edge[1])
    vis[edge[0]] = True
    vis[edge[1]] = True

    while (len(q) > 0):

        elem = q.popleft()

        for v in adj[elem]:

            if (vis[v] == False):
                q.append(v)

                vis[v] = True

                dis[v] = dis[elem] + 1

    count = 0

    for a in dis:

        if (a > dia/2):
            count += 1

    return count

main()
