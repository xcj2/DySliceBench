class segment_():
    def __init__(self,n,ide_ele,segfunc):
        self.ide_ele = ide_ele
        self.num = 1 << n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        self.segfunc = segfunc

    def update1(self, k):
        k += self.num
        self.seg[k] += 1
        while k:
            k >>= 1
            self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

    def query(self, p, q):
        if q < p:
            return self.ide_ele
        p += self.num;
        q += self.num
        res = self.ide_ele
        while p < q:
            if p & 1 == 1:
                res = self.segfunc(res, self.seg[p])
                p += 1
            if q & 1 == 1:
                q -= 1
                res = self.segfunc(res, self.seg[q])
            p >>= 1;
            q >>= 1
        return res

def main():
  import sys
  read = sys.stdin.buffer.read
  readline = sys.stdin.buffer.readline
  readlines = sys.stdin.buffer.readlines
  from operator import itemgetter

  N,M,Q = map(int,readline().split())
  S = segment_(N,0,lambda a, b: a+b)
  chk = []
  for i in range(M):
    L,R = map(int,readline().split())
    chk.append((1,L,R,i))
  for i in range(Q):
    l,r = map(int,readline().split())
    chk.append((2,l,r,i))

  chk.sort(key=itemgetter(2))
  ans = [0]*Q
  for a,l,r,i in chk:
    if a == 1:
      S.update1(l)
    else:
      ans[i] = S.query(l,r+1)

  print(*ans,sep='\n')
if __name__ == '__main__':
    main()