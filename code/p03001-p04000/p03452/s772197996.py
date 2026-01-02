#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.weight = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            if self.same_check(x, y) != True:
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            if self.same_check(x, y) != True:
               self.size[x] += self.size[y]
               self.size[y] = 0
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
               self.rank[rx] += 1

    def size(self, x):
        x = self.find(x)
        return self.size(x)

    def diff(self, x, y):
        if self.same_check(x, y) == True:
            return self.weight[x] - self.weight[y]
        else:
            print("inf")

#処理内容
def main():
	N, M = getlist()
	judge = "Yes"
	UF = WeightedUnionFind(N)
	for i in range(M):
		L, R, D = getlist()
		if UF.same_check(L - 1, R - 1):
			if UF.diff(L - 1, R - 1) != D:
				judge = "No"
				break
		else:
			UF.union(L - 1, R - 1, D)
	print(judge)



if __name__ == '__main__':
	main()