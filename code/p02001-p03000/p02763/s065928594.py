import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

class SegTree:
    def __init__(self, N):
        self.N = N
        self._N = 1<<((N-1).bit_length())
        self.node = [0]*2*self._N

    def build(self,lis):
        for i in range(self.N):
            self.node[i+self._N-1] = lis[i]
        for i in range(self._N-2,-1,-1):
            self.node[i] = self.node[i*2+1] | self.node[i*2+2]
        return

    def update(self,i,x):
        i += self._N-1
        self.node[i] = x
        while i:
            i = (i-1)>>1
            self.node[i] = self.node[i*2+1] | self.node[i*2+2]

    def query(self,p,q,idx=0,a=0,b=None):
        if b is None:
            b = self._N
        if q <= p or b <= p or q <= a:
            return 0
        elif p <= a and b <= q:
            return self.node[idx]
        else:
            res1 = self.query(p,q,idx*2+1,a,(a+b)//2)
            res2 = self.query(p,q,idx*2+2,(a+b)//2,b)
            return res1 | res2

n = ni()
oa = ord('a')
conv = lambda x: 1<<(ord(x)-oa) 
s = list(map(conv, list(input())))
q = ni()
S = SegTree(n)
S.build(s)
for _ in range(q):
    x,y,z = input().split()
    if x == '1':
        y = int(y)
        S.update(y-1, conv(z))
    else:
        y = int(y)
        z = int(z)
        # print(S.node[S._N-1:], y, z)
        v = S.query(y-1,z)
        # print(v, bin(v))
        print(str(bin(v)).count('1'))
