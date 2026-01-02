import heapq

def make_adj_list(v):
    adj_list = [[-1 for i in range(v)] for j in range(v)]
    return adj_list

def prim(adj_list, v, s):
    # スタートを0とする
    min_d = 0
    heap = []
    used = []
    for i in range(v):
        used.append(False)
    used[s] = True
    for i in range(v):
        if adj_list[s][i] != -1:
            heapq.heappush(heap, (adj_list[s][i], i))
        #　スタートからつなぐことができる辺をheapに入れる

    while len(heap) != 0:
        cost, to = heapq.heappop(heap)
        if used[to]:
            continue
        min_d += cost
        used[to] = True
        for i in range(v):
            if adj_list[to][i] != -1:
                heapq.heappush(heap, (adj_list[to][i], i)) 
            #集合に入れた頂点からつなぐことができる辺をheapに入れる

    return min_d

def main():
    v = int(input())
    adj_list = make_adj_list(v)
    for i in range(v):
        adj_list[i] = [int(j) for j in input().split()]
    min_d = prim(adj_list, v, 0)
    print(min_d)

if __name__ == "__main__":
    main()
