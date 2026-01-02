class SegTree:
    """ segment tree with point modification and range product. """
    # # https://yukicoder.me/submissions/452850
    def __init__(self, N, data_f = min, data_unit=1<<30):
        self.N = N
        self.data_f = data_f
        self.data_unit = data_unit
        self.data = [self.data_unit] * (N + N)

    def build(self, raw_data):
        data = self.data
        f = self.data_f
        N = self.N
        data[N:] = raw_data[:]
        for i in range(N - 1, 0, -1):
            data[i] = f(data[i << 1], data[i << 1 | 1])

    def set_val(self, i, x):
        data = self.data
        f = self.data_f
        i += self.N
        data[i] = x
        while i > 1:
            data[i >> 1] = f(data[i], data[i ^ 1])
            i >>= 1

    def fold(self, L, R):
        """ compute for [L, R) """
        vL = vR = self.data_unit
        data = self.data
        f = self.data_f
        L += self.N
        R += self.N
        while L < R:
            if L & 1:
                vL = f(vL, data[L])
                L += 1
            if R & 1:
                R -= 1
                vR = f(data[R], vR)
            L >>= 1
            R >>= 1
        return f(vL, vR)
      
N=int(input())
S=input()
data = [[0]*N for _ in range(26)]
di = {}
for i in range(N):
  data[ord(S[i])-97][i] = 1
  di[i] = S[i]

seg = [SegTree(N,max,0) for _ in range(26)]
for i in range(26):
  seg[i].build(data[i])
Q=int(input())
for i in range(Q):
  *q, = input().split()
  if q[0] == '1':
    i, c = q[1:]
    i = int(i)-1
    c_old = di[i]
    di[i] = c
    seg[ord(c_old)-97].set_val(i,0)
    seg[ord(c)-97].set_val(i,1)
  else:
    l,r = map(int,q[1:])
    ans=0
    for i in range(26):
      ans += seg[i].fold(l-1,r)
    print(ans)