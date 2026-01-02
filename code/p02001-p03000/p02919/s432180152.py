import sys
input = sys.stdin.readline
N = int(input())
P = list(map(int,input().split()))

'''
import random
N = 100000
P = list(range(1,N+1))
#random.shuffle(P)
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
            i = i//2
            j = j//2
        return s

P2 = [[[p,i],[0,0]] for i,p in enumerate(P)]

max2 = lambda x,y : sorted(x+y,reverse=True)[:2]

seg = SegmentTree(P2,max2,[[0,0],[0,0]])

cand = [[0,N]]

ans = 0
visited = set([])
while cand:
    #print(cand)
    temp = []
    for l,r in cand:
        if r-l < 2:
            continue
        if (l,r) in visited:
            continue
        visited.add((l,r))
        (m1,i1), (m2,i2) = seg.get(l,r)
        #print(P[l:r],m1,m2)
        i1,i2 = (i1,i2) if i1 < i2 else (i2,i1)
        ans += m2 * (i1-l+1) * (r-i2)
        temp.append([l,i2])
        temp.append([i1+1,r])
    cand = temp

print(ans)



