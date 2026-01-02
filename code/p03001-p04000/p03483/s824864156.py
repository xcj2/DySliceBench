import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import deque

# 右端のアルファベット：左端にもっていくとしてよい

S = [None] + [int(x) - ord('a') for x in read().rstrip()]

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

N = len(S) - 1
close = [False] * (N+1)

x_to_I = [deque() for _ in range(26)]
for i,x in enumerate(S[1:],1):
    x_to_I[x].append(i)

counter = [len(I) for I in x_to_I]
odd_cnt = sum(x&1 for x in counter)
if odd_cnt >= 2:
    print(-1)
    exit()

find_center = False
bit = BinaryIndexedTree([0] * (N+1))

answer = 0
for r in range(N,0,-1):
    x = S[r]
    bl = close[r]
    if bl:
        continue
    l = x_to_I[x][0]
    if l == r:
        find_center = True
        continue
    x_to_I[x].pop()
    x_to_I[x].popleft()
    costR = 1 if find_center else 0
    costL = l - 1 - bit.get_sum(l)
    bit.add(l,1)
    bit.add(r,1)
    close[l] = True
    answer += costL + costR

print(answer)