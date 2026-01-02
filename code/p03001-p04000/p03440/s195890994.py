class UnionFind():
    '''
    UnionFindでグラフの状態を管理する
    '''
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def find_root(self, x):
        '''
        ルートのノードを見つける
        '''
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        '''
        ノード同士を連結する
        '''
        x = self.find_root(x)
        y = self.find_root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    def is_same_group(self, x, y):
        '''
        同一のルーツを持つかどうか調査する
        '''
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.root[self.find_root(x)]


from heapq import heappop, heappush, heapify

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    union = UnionFind(N)
    for i in range(M):
        x, y = map(int, input().split())
        union.unite(x, y)
    select_node = 2 * (N- M - 1)
    if select_node > N:
        print("Impossible")
        return
    if N - 1 == M:
        print(0)
        return
    node = [0] * N
    qtable = [[] for _ in range(N)]
    allq = []
    for i in range(N):
        node[i] = union.find_root(i)
        heappush(qtable[node[i]], A[i])
    ans = 0
    cnt = 0
    for i in range(N):
        if qtable[i]:
            ans += heappop(qtable[i])
            cnt += 1
        allq.extend(qtable[i])

    heapify(allq)
    for i in range(select_node-cnt):
        ans += heappop(allq)
    print(ans)

main()
