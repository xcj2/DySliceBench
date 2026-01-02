import heapq
INF = 100000000000000

def make_adj_list(v):
    adj_list = []
    for i in range(v):
        adj_list.append([])
    return adj_list

def dijkstra(v, e, adj_list, s):
    heap = []
    d = []
    pre = []
    for i in range(v):
        d.append(INF)
        pre.append(s)
    d[s] = 0
    heapq.heappush(heap, (0, s))
    while len(heap) != 0:
        candidate_d, now_v = heapq.heappop(heap)
        if d[now_v] < candidate_d:
            continue
        for v, cost in adj_list[now_v]:
            if d[v] > d[now_v] + cost:
                d[v] = d[now_v] + cost
                heapq.heappush(heap,(d[v], v))
                pre[v] = now_v
    return d, pre

def main():
    v, e, s = map(int, input().split())
    adj_list = make_adj_list(v)
    for i in range(e):
        a = [int(i) for i in input().split()]
        adj_list[a[0]].append((a[1], a[2]))
        
    d, pre = dijkstra(v, e, adj_list, s)

    for i in range(v):
        if d[i] == INF:
            print("INF")
        else:
            print(d[i])

if __name__ == "__main__":
    main()
