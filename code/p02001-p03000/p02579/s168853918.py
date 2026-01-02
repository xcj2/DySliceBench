from operator import itemgetter, attrgetter
import sys
readlines = sys.stdin.readlines
input = sys.stdin.readline
 
class RadixHeap:
    def __init__(self, C=1 << 31):
        self.last = 0
        self.size = 0
        self.v = [[] for _ in range(C.bit_length()+1)]
 
    def push(self, key, val):
        self.size += 1
        self.v[(key ^ self.last).bit_length()].append((key, val))
 
    def pop(self):
        v = self.v
        if not v[0]:
            i = 1
            while not v[i]:
                i += 1
            vi = v[i]
            new_last, _ = min(vi, key=itemgetter(0))
            for key, val in vi:
                v[(key ^ new_last).bit_length()].append((key, val))
            self.last = new_last
            vi.clear()
        self.size -= 1
        return v[0].pop()
 
    def __len__(self): return self.size

H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
Ch -= 1;Cw -= 1
Dh -= 1;Dw -= 1
S = readlines()
 
INF = 10**10
D = [[INF]*W for _ in [0]*H]
 
q = RadixHeap()
q.push(0, Ch*W+Cw)
 
while q:
    d, ij = q.pop()
    i, j = divmod(ij, W)
 
    for di in range(-2, 3):
        for dj in range(-2, 3):
            if di == dj == 0:
                continue
            I = i+di
            J = j+dj
            if 0 <= I < H and 0 <= J < W and S[I][J] == '.':
                if abs(di)+abs(dj) == 1:
                    if D[I][J] <= d:
                        continue
                    D[I][J] = d
                    q.push(d, I*W+J)
                else:
                    if D[I][J] <= d+1:
                        continue
                    D[I][J] = d+1
                    q.push(d+1, I*W+J)
 
ans = D[Dh][Dw]
print(ans if ans < INF else -1)