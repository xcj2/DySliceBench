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
    H,W,A,B = LI()

    ans = [0]*(W-B)

    ans[0] = 1

    for i in range(1,B+H-A):
        ans[0] *= i
        ans[0] %= mod
    for i in range(1,A-1+W-B):
        ans[0] *= i
        ans[0] %= mod
    for i in range(1,H-A):
        ans[0] *= pow(i,mod-2,mod)
        ans[0] %= mod
    for i in range(1,B+1):
        ans[0] *= pow(i,mod-2,mod)
        ans[0] %= mod
    for i in range(1,W-B):
        ans[0] *= pow(i,mod-2,mod)
        ans[0] %= mod
    for i in range(1,A):
        ans[0] *= pow(i,mod-2,mod)
        ans[0] %= mod

    for i in range(1,W-B):
        ans[i] = ans[i-1]
        ans[i] *= (B+H-A-1+i)
        ans[i] %= mod
        ans[i] *= (W-B-i)
        ans[i] %= mod
        ans[i] *= pow(B+i,mod-2,mod)
        ans[i] %= mod
        ans[i] *= pow(A-1+W-B-i,mod-2,mod)
        ans[i] %= mod

    return(sum(ans)%mod)


if __name__ == "__main__":
    print(main())
