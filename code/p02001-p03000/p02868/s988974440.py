def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
import heapq
# import math
INF = 10**11

def main():
    n, m= getList()
    begin = [[] for i in range(n)]
    cost = [-1 for i in range(n)]
    for i in range(m):
        st, en, cos = getList()
        begin[st-1].append((cos, en-1))

    h = []
    for warp in begin[0]:
        heapq.heappush(h, warp)
    cur_mas = 0

    while(h):
        cand = heapq.heappop(h)
        if cand[1] > cur_mas:
            # 歩を1つ進め、その場所を更新
            cur_mas += 1
            cost[cur_mas] = cand[0]
            for warp in begin[cur_mas]:
                # そこまでの距離とコストを足す
                tcos, ten = warp[0] + cost[cur_mas], warp[1]
                heapq.heappush(h, (tcos, ten))
            heapq.heappush(h, cand)



    print(cost[n-1])
if __name__ == "__main__":
    main()