#和のセグ木にするときは以下の関数を定義する必要あり。
def segfunc(x,y):
  return x+y

class SegmentTree(object):
    def __init__(self, A, dot, unit):
        n = 1 << (len(A) - 1).bit_length()
        tree = [unit] * (2 * n)
        for i, v in enumerate(A):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n = n
        self._tree = tree
        self._dot = dot
        self._unit = unit

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def update(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])

    def add(self, i, v):
        self.update(i, self[i] + v)

    def sum(self, l, r): #これで[l,r)から取り出す。
        l += self._n
        r += self._n
        l_val = r_val = self._unit
        while l < r:
            if l & 1:
                l_val = self._dot(l_val, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self._dot(self._tree[r], r_val)
            l >>= 1
            r >>= 1
        return self._dot(l_val, r_val)


N,M,Q = map(int,input().split())
A = []
for i in range(M):
  a,b = map(int,input().split())
  A.append([a,b,-1]) #-1は鉄道
for i in range(Q):
  a,b = map(int,input().split())
  A.append([a,b,i]) #iはクエリのID。出力でIDの順に並べる
A.sort(key=lambda x : x[1]) #終点でソート
MAX = 510
Range = [0 for _ in range(MAX)]
Tree = SegmentTree(Range,segfunc,0)
#print(A)
ans = [-1 for _ in range(Q)]
for i in range(M+Q):
  a,b,ID = A[i]
  if ID == -1:
    Tree.add(a,1)
  else:
    temp = Tree.sum(a,b+1) #セグ木の取得は開区間なのでb+1
    ans[ID] = temp
#print(ans)
print(*ans,sep="\n")
    
