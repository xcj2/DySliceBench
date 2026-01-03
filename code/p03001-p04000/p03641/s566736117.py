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
read = sys.stdin.read
readline = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,*p = map(int,read().split())

INF = 1<<30
p += [INF,INF]

def argmin(i,j):
    if p[i] < p[j]: return i
    else: return j

even = segment_tree(n//2+1,argmin,n)
odd = segment_tree(n//2+1,argmin,n+1)

even.build(range(0,n+2,2))
odd.build(range(1,n+2,2))

ans = [0]*n

def get(i,j):
    return odd.query(i//2,(j-1)//2)  if i%2 else even.query(i//2,(j-1)//2)

from heapq import *
k = get(0,n-1)
q = [(p[k],k,0,n-1)]

for I in range(n//2):
    v,k,i,j = heappop(q)
    l = even.query((k+1)//2,j//2) if i%2 else odd.query((k+1)//2,j//2)
    
    #print(v,p[l])
        
    ans[2*I] = v
    ans[2*I+1] = p[l]
    
    if i < k+1:
        kk = get(i,k-1)
        heappush(q,(p[kk],kk,i,k-1))
    if k+1<l-1:
        kk = get(k+1,l-1)
        heappush(q,(p[kk],kk,k+1,l-1))
    if l+1 < j:
        kk = get(l+1,j)
        heappush(q,(p[kk],kk,l+1,j))
    
print(*ans)



#x = merge3([[1,0],[4,0]],[[2,0]],[[3,0],[6,0]])
#print(x)
