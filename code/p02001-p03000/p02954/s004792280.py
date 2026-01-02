import sys
import heapq
import bisect

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(sys.stdin.readline()[:-1])
def IR(n): return([I() for _ in range(n)])

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return a * b // GCD(a,b)

def Eratosthenes(N):
    r = [True]*(N+1)
    r[0] = False
    r[1] = False
    i = 2
    while i*i<=N:
        if r[i]: 
            j = i
            while i*j<=N:
                prime[i*j]=False
                j+=1
        i+=1
    return(r)

def main():
    s = S()
    N = len(s)

    R = [0] * N
    R[0] = 1
    L = [0] * N
    L[-1] = 1

    for i in range(1,N):
        if s[i] == "R":
            R[i] = R[i-1] + 1
            R[i-1] = 0
    for i in range(N-2,-1,-1):
        if s[i] == "L":
            L[i] = L[i+1] + 1
            L[i+1] = 0

    ans = [0]*N
    for i in range(N-1):
        if R[i] > 0:
            ans[i] = (R[i]+1)//2 + L[i+1]//2
    for i in range(1,N):
        if L[i] > 0:
            ans[i] = (L[i]+1)//2 + R[i-1]//2

    return(" ".join(map(str,ans)))
    

if __name__ == "__main__":
    print(main())
