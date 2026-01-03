class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        """
        :param int size:
        """
        self.bit = [0 for _ in range(size)]
        self.size = size

    def add(self, i, w):
        """
        i番目にwを加える
        :param int i:
        :param int w:
        :return:
        """
        x = i + 1
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        """
        [0,i]の合計
        :param int i:
        :return:
        """
        res = 0
        x = i + 1
        while x > 0:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def search(self, x):
        """
        二分探索。和がx以上となる最小のインデックス(>= 1)を返す
        :param int x:
        :return :
        """
        i = 0
        s = 0
        step = 1 << self.size.bit_length()
        while step:
            if i + step <= self.size and s + self.bit[i + step - 1] < x:
                print(self.bit[i + step - 1], i, step)
                i += step
                s += self.bit[i - 1]
            step >>= 1
        return i

    def __len__(self):
        return self.size
from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
for i in range(n):
  d[a[i]]=i+1
Bit = BinaryIndexedTree(n+1)
ans=0
for i in range(n):
  j=i+1
  i=d[j]
  x=Bit.sum(i)
  ok=i
  ng=-1
  while ok - ng > 1:
    mid=(ok+ng)//2
    if Bit.sum(mid)==x:
      ok=mid
    else:
      ng=mid
  l=ok+1
  ok=i
  ng=n+1
  while ng - ok > 1:
    mid=(ok+ng)//2
    if Bit.sum(mid)==x:
      ok=mid
    else:
      ng=mid
  r=ok
  ans+=j*(i-l+1)*(r-i+1)
  Bit.add(i,1)
print(ans)
  