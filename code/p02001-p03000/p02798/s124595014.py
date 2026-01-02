from itertools import combinations

class BinaryIndexedTree():
    def __init__(self, seq):
        self.size = len(seq)
        self.depth = self.size.bit_length()
        self.build(seq)
        
    def build(self,seq):
        data = seq
        size = self.size
        for i,x in enumerate(data):
            j = i+(i&(-i))
            if j < size:
                data[j] += data[i]
        self.data = data
        
    def __repr__(self):
        return self.data.__repr__()
        
    def get_sum(self,i):
        data = self.data
        s = 0
        while i:
            s += data[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        data = self.data
        size = self.size
        while i < size:
            data[i] += x
            i += i & -i
    
    def find_kth_element(self,k):
        data = self.data; size = self.size
        x,sx = 0,0
        dx = 1 << (self.depth)
        for i in range(self.depth - 1, -1, -1):
            dx = (1 << i)
            if x + dx >= size:
                continue
            y = x + dx
            sy = sx + data[y]
            if sy < k:
                x,sx = y,sy
        return x + 1

def Inversion(seq):
    seq = [i + 1 for i in seq]
    # seqは、1,2,...,Nの順列 (0-indexだったので合わせた。)
    N = len(seq)
    bit = BinaryIndexedTree([0] * (N+1))
    inv = N*(N-1)//2
    for x in seq:
        inv -= bit.get_sum(x)
        bit.add(x,1)
    return inv

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 偶数/奇数の位置に来るindex達を生成する。Combinations(range(N), N//2)
# 偶数だけの列と奇数だけの列を作って、それぞれソート。(転倒数を計算したいので、valとともにindex番号も持っておく)
# 数字と位置の偶奇が異なる場合はB面、一致しているときはA面を使う。
# 上記の２つの数列を一つにまとめた時に広義単調増加になっているかを判定。
# 最小の移動回数が答え。存在しない場合は-1
# 最小の操作回数⇒転倒数

# combinations(n, n//2)が偶数の位置に来るindex。
ptn = list(combinations(range(N), N//2))

ans = - 1
for p in ptn:
  evnline = []
  oddline = []
  for i in range(N):
    if i in p:
      evnline.append((A[i] if (i + 1) % 2 == 0 else B[i], i))
    else:
      oddline.append((B[i] if (i + 1) % 2 == 0 else A[i], i))
  line = [0] * N
  evnline.sort()
  oddline.sort()
#   print("e, o", evnline, oddline)
  for itr, val in enumerate(evnline):
    line[itr * 2 + 1] = val
  for itr, val in enumerate(oddline):
    line[itr * 2] = val
  if all([j[0] >= i[0] for i, j in zip(line,line[1:])]):
    exchange_cnt = Inversion([i[1] for i in line])
    if ans == -1:
      ans = exchange_cnt
    else:
      ans = min(ans, exchange_cnt)

print(ans)
