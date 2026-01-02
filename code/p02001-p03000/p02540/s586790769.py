
class SegTree:  # モノイドに対して適用可能、Nが2冪でなくても良い
    def __init__(self ,N ,seg_func ,unit):
        self.N = 1 << ( N -1).bit_length()
        self.func = seg_func
        self.unit = unit
        self.tree = [self.unit ] *( 2 *self.N)

    def build(self ,init_value):  # 初期値を[N,2N)に格納
        for i in range(len(init_value)):
            self.tree[ i +self.N] = init_value[i]
        for i in range(self. N -1 ,0 ,-1):
            self.tree[i] = self.func(self.tree[i << 1] ,self.tree[i << 1 | 1])

    def set_val(self ,i ,x):  # i番目(0-index)の値をxに変更
        i += self.N
        self.tree[i] = x
        i >>= 1
        while i:
            self.tree[i] = self.func(self.tree[i << 1] ,self.tree[i << 1 | 1])
            i >>= 1

    def fold(self ,L ,R):  # [L,R)の区間取得
        L += self.N
        R += self.N
        vL = self.unit
        vR = self.unit
        while L < R:
            if L & 1:
                vL = self.func(vL ,self.tree[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.tree[R] ,vR)
            L >>= 1
            R >>= 1
        return self.func(vL ,vR)



class DSU:
  def __init__(self, n):
    self.n = n
    self.root = [-1] * (n + 1)
    self.rank = [0] * (n + 1)
  def leader(self, x):
    rt = self.root[x]
    if rt < 0: return x
    else: self.root[x] = self.leader(rt)
    return self.root[x]
  def merge(self, x, y):
    leader = self.leader
    xrt = leader(x)
    yrt = leader(y)
    if xrt == yrt: return
    if self.rank[xrt] > self.rank[yrt]:
      self.root[xrt] += self.root[yrt]
      self.root[yrt] = xrt
    else:
      self.root[yrt] += self.root[xrt]
      self.root[xrt] = yrt
      self.rank[yrt] += self.rank[xrt] == self.rank[yrt]
  def same(self, x, y): return self.leader(x) == self.leader(y)
  def size(self, x):  return -self.root[self.leader(x)]
  def group(self):
    n = self.n
    leader = self.leader
    res = [[] for _ in range(n + 1)]
    for x in range(n + 1): res[leader(x)].append(x)
    return [res[i] for i in range(n + 1) if len(res[i])]


def main():
    n, q = map(int, input().split())
    dsu = DSU(n)
    for _ in range(q):
        t, u, v = map(int, input().split())
        if t == 0:
            dsu.merge(u, v)
        else:
            print(1 if dsu.same(u, v) else 0)


def seg_func(x,y):
    if x[0] > y[0]:
        return x
    else:
        return y
def seg_func1(x,y):
    if x[0] < y[0]:
        return x
    else:
        return y

n = int(input())
X = []
for xx in range(n):

    a, b = map(int, input().split())
    X.append([xx, a, b])

X = sorted(X, key=lambda x: x[1])

dsu = DSU(n)
tree = SegTree(n+1,seg_func,[-1,-1])

for  v in X:
    tree.set_val(v[2], [v[2], v[0]])
    get = tree.fold(0, v[2])
    if get[0] != -1:
        dsu.merge(get[1], v[0])

X = sorted(X, reverse=True, key=lambda x: x[1])

tree = SegTree(n+2,seg_func,[-1,-1])

for v in X:
    tree.set_val(v[2], [v[2],v[0]])
    get = tree.fold(v[2]+1, n+2)
    if get[0] != -1:
        dsu.merge(get[1], v[0])

groups = dsu.group()
ans = [0] * (n * 2 + 10)

for a in groups:
    count = len(a)
    for v in a:
        ans[v]=count

for l, v in enumerate(ans):
    if l < n:
        print(str(v))
    else:
        exit()

