import queue
def dist(graph, start):
    q = queue.Queue()
    rtn = [None]*len(graph)
    q.put(start)
    rtn[start] = 0
    while not q.empty():
        target = q.get()
        for index in graph[target]:
            if rtn[index] is None:
                q.put(index)
                rtn[index] = rtn[target] + 1
    return rtn

def solve(dist_t, dist_a):
    ans = 0
    for i in range(len(dist_t)):
        if dist_t[i] < dist_a[i]:
            if ans < dist_a[i] - 1:
                ans = dist_a[i] - 1
    return ans

def main():
    n, u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    dist_t = dist(graph, u)
    dist_a = dist(graph, v)
    print(solve(dist_t, dist_a))

if __name__ == "__main__":
    main()