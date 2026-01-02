class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    # 部分集合とその要素数を返す
    def subsetall(self):
        a = []
        for i in xrange(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a

N, M = map(int, input().split())
p = list(map(int, input().split()))

s = UnionFind(N)

for i in range(M):
  a, b = map(int, input().split())
  s.union(a-1,b-1)

ans = 0
for i in range(N):
  if p[i] == i+1: ans +=1
  elif s.find(p[i]-1) == s.find(i): ans+=1
print(ans)