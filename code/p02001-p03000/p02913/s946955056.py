import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    def zalgo(S):
        A=[0]*len(S)
        A[0]=len(S)
        i,j=1,0
        while i<len(S):
            while i+j<len(S) and S[j]==S[i+j]:
                j+=1
            A[i]=j 
            if j==0:
                i+=1
                continue
            k=1
            while i+k<len(S) and k+A[k]<j:
                A[i+k]=A[k]
                k+=1
            i+=k
            j-=k
        return A
    N=int(input())
    S=input()
    ans=0
    for i in range(N-1):
        A=zalgo(S[i:])
        for j,x in enumerate(A):
            if x>j:
                ans=max(ans,j)
            else:
                ans=max(ans,x)
    print(ans)

if __name__ == '__main__':
    main()
