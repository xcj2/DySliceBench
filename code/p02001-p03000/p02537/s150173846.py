N,K=map(int,input().split())

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

A=[int(input()) for _ in range(N)]
seg = SegTree(300005,max,0)
seg.build([0]*300005)
for i in range(N):
  a = A[i]
  tmp = seg.fold(max(0,a-K),min(300005,a+K+1))
  seg.set_val(a,tmp+1)

print(seg.fold(0,300005))