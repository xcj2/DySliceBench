N,K = map(int,input().split())
*A, = map(lambda x:(int(x)%K-1)%K,input().split())

class cumulative_sum:
    def __init__(self,A):
        N = len(A)
        self.S = [0]*(N+1)
        for i in range(N):
            self.S[i+1] = (self.S[i] + A[i])%K
    def get(self,i,j=None):
        if j==None:j=len(self.S)-1
        if j<=i:return 0
        return (self.S[j]-self.S[i])%K

SumA = cumulative_sum(A)

def binary_search(l,r,func):
    if func(l):return l-1
    if not func(r):return r
    while l+1<r:
        i = (l+r)//2
        if func(i):
            r = i
        else:
            l = i
    return l

def f(j):
    return cnt[s][j] > idx - K

ans = 0
cnt = {}
for idx,s in enumerate(SumA.S):
    if not s in cnt:
        cnt[s] = [-2*K]
    cnt[s].append(idx)
    l = len(cnt[s])
    j = binary_search(0,l-1,f)
    ans += (l-1)-(j+1)
print(ans)