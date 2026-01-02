import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

'''
import random
N = 200000
A = [random.randint(1,10**9) for i in range(N)]
#A = [1]*N
B = A[:]
for i in range(200000):
    j = random.randint(0,N-1)
    #j = 1
    B[j] += B[j-1] + B[(j+1)%N]
    '''

class SegmentTree:
    def __init__(self,data,op,default):
        N = len(data)
        self.N = N
        self.op = op
        self.default = default
        self.l = 2**((N-1).bit_length())
        self.data = [default]*self.l + data + [default]*(self.l-N)
        for i in range(self.l-1,0,-1):
            self.data[i] = op(self.data[2*i], self.data[2*i+1])

    def get_data(self):
        return self.data[self.l:self.l + self.N]

    def set(self,i,val):
        i += self.l
        self.data[i] = val
        i = i//2
        while i > 0:
            self.data[i] = self.op(self.data[2*i], self.data[2*i+1])
            i = i//2

    def get(self,i,j):
        i += self.l
        j += self.l
        s = self.default 
        while j-i > 0:
            if i & 1:
                s = self.op(s,self.data[i])
                i += 1
            if j & 1:
                s = self.op(s,self.data[j-1])
                j -= 1
            i, j = i//2, j//2
        return s

D = [b-a for b,a in zip(B,A)]
D = [(d,i) for i,d in enumerate(D)]

inf = 10**16
seg = SegmentTree(D,max,(-inf,-inf))

cnt = 0
while True:
    m, i = seg.get(0,N)
    if m == 0:
        break
    l = B[i-1]
    r = B[(i+1) % N]
    diff = l+r
    n = (m - max(l,r)-1)//diff + 1
    if n <= 0 or m-diff*n < 0:
        print(-1)
        exit()
    seg.set(i,(m-diff*n,i))
    B[i] -= diff*n
    cnt += n

print(cnt)

