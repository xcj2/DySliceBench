import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

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
            i = i//2
            j = j//2
        return s

AI = [(a,i) for i,a in enumerate(A)]

inf = 10**10
seg = SegmentTree(AI,min,(inf,inf))

cand = [(0,N)]

ans = 0
while cand:
    temp = []
    for l,r in cand:
        m, i = seg.get(l,r)
        ans += m * (i-l+1) * (r-i)
        if l < i:
            temp.append([l,i])
        if i+1 < r:
            temp.append([i+1,r])
    cand = temp

print(ans)


