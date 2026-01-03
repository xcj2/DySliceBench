from collections import defaultdict
con = 300000

def getlist():
	return list(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            if self.same_check(x, y) != True:
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[x] = y
        else:
            if self.same_check(x, y) != True:
               self.size[x] += self.size[y]
               self.size[y] = 0
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
               self.rank[x] += 1

    def siz(self, x):
        x = self.find(x)
        return self.size[x]

#処理内容
def main():
	#受け取り、処理
	N, K, L = getlist()
	UFp = UnionFind(N)
	UFr = UnionFind(N)
	for i in range(K):
		p, q = getlist()
		UFp.union(p, q)
	for i in range(L):
		r, s = getlist()
		UFr.union(r, s)

	for i in range(1, N):
		UFp.find(i)
		UFr.find(i)

	s1 = UFp.par
	s2 = UFr.par
	s3 = []
	
	for i in range(1, N + 1):
		s3.append([s1[i], s2[i]])

	#前計算
	D = defaultdict(int)
	for i in range(N):
		a = s3[i][0]
		b = s3[i][1]
		D[a * con + b] += 1
	#答え
	ans = []
	for i in range(N):
		ans.append(D[s3[i][0] * con + s3[i][1]])
	print(" ".join(list(map(str, ans))))

if __name__ == '__main__':
	main()