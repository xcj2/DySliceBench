import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from operator import itemgetter, mul
from functools import reduce

N = int(readline())
A = list(map(int,readline().split()))
B = list(map(int,readline().split()))
C = list(map(int,readline().split()))

sgn = [0] * N
for i,(a,b,c) in enumerate(zip(A,B,C)):
    if a == b-1 and c == b+1:
        sgn[i] = 1
    elif a == b+1 and c == b-1:
        sgn[i] = -1
    else:
        print('No')
        exit()

if any(x%6 != 2 for x in B[::2]) or any(x%6 != 5 for x in B[1::2]):
    print('No')
    exit()

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
    # seqは、1,2,...,Nの順列
    N = len(seq)
    bit = BinaryIndexedTree([0] * (N+1))
    inv = N*(N-1)//2
    for x in seq:
        inv -= bit.get_sum(x)
        bit.add(x,1)
    return inv

OD = sorted(enumerate(B[::2],1), key=itemgetter(1))
ind, val = zip(*OD)
od_inv = Inversion(ind)

EV = sorted(enumerate(B[1::2],1), key=itemgetter(1))
ind, val = zip(*EV)
ev_inv = Inversion(ind)

od_sgn = reduce(mul, sgn[::2])
ev_sgn = reduce(mul, sgn[1::2])

condition = (od_sgn == (-1)**ev_inv) and (ev_sgn == (-1)**od_inv)

answer = 'Yes' if condition else 'No'
print(answer)