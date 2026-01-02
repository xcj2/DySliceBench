class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.parent = [i for i in range(n + 1)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n + 1)
        # 木の要素数
        self.size = [1] * (n + 1)

        self.score = n * (n - 1) // 2

    # 検索
    def find(self, x):
        if self.parent[x] == x:  # 根ならその番号を返す
            return x
        else:  # 走査していく過程で親を書き換える
            self.parent[x] = self.find(self.parent[x])

            return self.parent[x]

    # 併合
    def union(self, x, y):
        # 根を探す
        parent_x = self.find(x)
        parent_y = self.find(y)

        if(parent_x != parent_y):
            if self.rank[parent_x] == self.rank[parent_y]: 
                # 木の高さが同じなら片方を1増やす
                self.rank[parent_x] += 1  # ここのxとyはどちらでも良い
            elif self.rank[parent_x] < self.rank[parent_y]:  
                # 木の高さを比較し、低いほうから高いほうに辺を張る
                parent_x, parent_y = parent_y, parent_x

            self.score -= self.size[parent_x] * self.size[parent_y]
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]

    def getsize(self, x):
        return self.size[self.find(x)]

    def same_check(self, x, y):  # 同じ集合に属するか判定
        return self.find(x) == self.find(y)


def main():
    N, M = (int(i) for i in input().split())
    AB = [[int(i) for i in input().split()] for i in range(M)]

    uni = UnionFind(N)

    score_list = []
    for i in range(M-1, -1, -1):
        inp = AB[i]
        score_list.append(uni.score)
        uni.union(inp[0], inp[1])

    print(*score_list[::-1], sep="\n")

if __name__ == "__main__":
    main()
