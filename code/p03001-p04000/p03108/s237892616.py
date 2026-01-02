class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1 for _ in range(n+1)]

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
    
def main():
    N, M = [int(_) for _ in input().split()]
    bridge = [tuple(map(int, input().split())) for _ in range(M)]

    last = []
    last.append(int(N * (N-1) * 0.5))

    ins = UnionFind(N)
    last_temp = 0

    for i in range(M-1):
        #print(ins.par)
        if ins.same_check(bridge[M-1-i][0],bridge[M-1-i][1]):
            last.append(last[-1])
            #ins.union(bridge[M-1-i][0],bridge[M-1-i][1])
        else:
            last_temp = last[-1] - (ins.size[ins.find(bridge[M-1-i][0])]) * (ins.size[ins.find(bridge[M-1-i][1])])
            #print(ins.size,i)
            last.append(last_temp)
            ins.union(bridge[M-1-i][0],bridge[M-1-i][1])
    
    [print(last[M-i-1]) for i in range(M)]
    exit()
    
main()