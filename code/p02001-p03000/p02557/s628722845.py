
class segment_tree:
    def __init__(self, N, operator_M, e_M):
        self.op_M = operator_M
        self.e_M = e_M
        
        self.N0 = 1<<(N-1).bit_length()
        self.dat = [self.e_M]*(2*self.N0)
    
    # 長さNの配列 initial で初期化
    def build(self, initial):
        self.dat[self.N0:self.N0+len(initial)] = initial[:]
        for k in range(self.N0-1,0,-1):
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])

    # a_k の値を x に更新
    def update(self,k,x):
        k += self.N0
        self.dat[k] = x
        k //= 2
        while k:
            self.dat[k] = self.op_M(self.dat[2*k], self.dat[2*k+1])
            k //= 2

    # 区間[L,R]をopでまとめる
    def query(self,L,R):
        L += self.N0; R += self.N0 + 1 
        sl = sr = self.e_M
        while L < R:
            if R & 1:
                R -= 1
                sr = self.op_M(self.dat[R],sr)
            if L & 1:
                sl = self.op_M(sl,self.dat[L])
                L += 1
            L >>= 1; R >>= 1
        return self.op_M(sl,sr)

    def get(self, k): #k番目の値を取得。query[k,k]と同じ
        return self.dat[k+self.N0]

# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = map(int,readline().split())
*a, = map(int,readline().split())
*b, = map(int,readline().split())

ca = [0]*(n+1)
cb = [0]*(n+1)

for i in a: ca[i] += 1
for i in b: cb[i] += 1


from heapq import *

qc = [0]*(n+1)
for i,(x,y) in enumerate(zip(ca,cb)):
    if x+y > n:
        print("No")
        exit()
    elif i==0 or x+y==0:
        continue
    else:
        qc[i] = x+y


def op(a,b):
    if qc[a] <= qc[b]: return b
    else: return a

s = segment_tree(n+1,op,0)
s.build(list(range(n+1)))

sa = set(a)
sb = set(b)

def dela(j):
    ca[j] -= 1
    if ca[j]==0:
        sa.remove(j)
    
def delb(j):
    cb[j] -= 1
    if cb[j]==0:
        sb.remove(j)

ans = [None]*n
for i in range(n):
    j = s.dat[1]
    #print(i,sa,sb,v,j)
    #print(j,qc,s.dat)
    if ca[j]:
        dela(j)

        for k in sb:
            if k != j: break
        delb(k)
        ans[i] = (j,k)

    else:
        delb(j)
        
        for k in sa:
            if k != j: break
        dela(k)
        ans[i] = (k,j)
    
    qc[j] -= 1
    qc[k] -= 1
    s.update(j,j)
    s.update(k,k)

from operator import itemgetter
ans.sort(key=itemgetter(0))

print("Yes")
ans = [y for x,y in ans]
print(*ans)










    
    
    