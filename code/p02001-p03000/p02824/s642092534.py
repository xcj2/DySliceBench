class cumulative_sum:
    def __init__(self,A):
        N = len(A)
        self.S = [0]*(N+1)
        for i in range(N):
            self.S[i+1] = self.S[i] + A[i]
    def get(self,i,j=None):
        if j==None:j=len(self.S)-1
        if j<=i:return 0
        return self.S[j]-self.S[i]

N,M,V,P = map(int,input().split())
*A, = map(int,input().split())
A.sort()

S = cumulative_sum(A)

def check(i):
    s = max(0,S.get(i+1,N-P+1))
    res = max(M*(V-P-i),0)
    if A[i]+M<A[N-P]: return False
    return ((A[i]+M)*max(0,N-P-i))>=s+res

ans = sum(check(i) for i in range(N))
print(ans)