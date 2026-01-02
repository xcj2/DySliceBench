class UnionFind():
    # コンストラクタ
    def __init__(self, n):
        # 要素数
        self.n = n
        # parents[i]: 要素iの親要素の番号
        # 要素iが根の場合、parents[i] = -(そのグループの要素数)
        self.parents = [-1] * n
 
    # 要素xが属するグループの根を返す
    # 経路圧縮
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    # 要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]
 
    # 要素x,yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    # 全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    # グループの数を返す
    def group_count(self):
        return len(self.roots())

def main():
    N,M,K = map(int,input().split())

    best_friend = [0] * N
    friend = UnionFind(N)
    for _ in range(M):
        A,B = map(int,input().split())
        best_friend[A-1] += 1
        best_friend[B-1] += 1
        friend.union(A-1, B-1)

    blocked = [[] for _ in range(N)]
    for _ in range(K):
        C,D = map(int,input().split())
        blocked[C-1].append(D-1)
        blocked[D-1].append(C-1)

    ans = [0] * N
    for i in range(N):
        # 友達候補 - 友達 - 自分
        ans[i] = friend.size(i) - best_friend[i] - 1
        # 嫌いな人は友達になれない
        for bad in blocked[i]:
            if friend.same(i, bad):
                ans[i] -= 1

    print(*ans, sep=" ")

if __name__ == "__main__":
    main()