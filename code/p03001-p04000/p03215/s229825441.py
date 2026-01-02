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
def main():
    N,K = map(int,input().split())
    *A, = map(int,input().split())
    SA = cumulative_sum(A)
    B = {}

    for i in range(N):
        for j in range(i+1,N+1):
            s = SA.get(i,j)
            B[s] = B.get(s,0)+1

    ans = 0
    for i in range(40,-1,-1):
        x = ans + (1<<i)
        c = sum(n for b,n in B.items() if b&x==x)
        if c>=K:ans = x
    print(ans)
main()