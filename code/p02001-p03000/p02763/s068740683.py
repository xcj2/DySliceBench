def segfunc(x,y):
  return x|y

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


N = int(input())
S = str(input());Q = int(input())
A = []
for i in range(N):
  temp = S[i]
  num = ord(temp) - 97
  A.append(pow(2,num))
Tree = SegmentTree(A, segfunc, 0)
for i in range(Q):
  query = list(map(str,input().split()))
  if query[0] == "1":
    loc = int(query[1])-1 #0index
    num = ord(query[2])-97
    Tree.update(loc,pow(2,num))
  else:
    left = int(query[1])-1
    right = int(query[2])-1
    ret = Tree.sum(left,right+1)
    ans = 0
    for j in range(26):
      if (ret>>j)&1 == 1:
        ans += 1
    print(ans)
