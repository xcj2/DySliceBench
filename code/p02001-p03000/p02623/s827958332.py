import bisect
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF = 10**20
def main():
    N,M,K=mi()
    A=[0]+list(mi())
    B=[0]+list(mi())

    v = [0]*(N+1)
    u = [0]*(M+1)

    for i in range(N):
        v[i+1] = A[i+1] + v[i]
        
    for i in range(M):
        u[i+1] = B[i+1] + u[i]

    # print(u,v)
    ans = 0
    for i in range(M+1):
        if K-u[i] < 0: continue
        j = bisect.bisect_left(v,K-u[i])

        if j == 0 and K-u[i] < A[0]: continue

        if j<len(v) and v[j] != K-u[i]:
            j -= 1
        
            
        ans = max(ans,i+j)

    print(ans)



if __name__ == "__main__":
    main()
