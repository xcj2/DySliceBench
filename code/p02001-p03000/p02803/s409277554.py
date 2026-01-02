from heapq import heappush, heappop
def main():
    def dijkstra_search(s):
        d = [INF] * size
        searched = [False] * size
        d[s] = 0
        searched[s] = True
        edge_list = []
        count = 1
        for i in edge[s]:
            heappush(edge_list,i)
        while edge_list:
            min_d,min_v = heappop(edge_list)
            if searched[min_v] or min_d > d[min_v]:
                continue
            v = min_v
            d[v] = min_d
            searched[v] = True
            count += 1
            for i,j in edge[v]:
                next_d = i+d[v]
                if not searched[j]:
                    heappush(edge_list,(next_d,j))
            if count == size:
                break
        return d
    def judge(a,b):
        if a >= 0 and a < h and b >= 0 and b < w and s[a][b] == ".":
            return True
        else:
            return False
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    size = h*w
    INF = float('inf')
    edge = [[] for _ in range(size)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                if judge(i+1,j):
                    edge[i*w+j].append((1,((i+1)*w+j)))
                if judge(i-1,j):
                    edge[i*w+j].append((1,((i-1)*w+j)))
                if judge(i,j+1):
                    edge[i*w+j].append((1,(i*w+(j+1))))
                if judge(i,j-1):
                    edge[i*w+j].append((1,(i*w+(j-1))))
    ans = []
    for i in range(size):
        if s[i//w][i%w-1] == ".":
            d_list = dijkstra_search(i)
            for j in d_list:
                if not j == INF:
                    ans.append(j)
    print(max(ans))
    
if __name__ == '__main__':
    main()