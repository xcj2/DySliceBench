import sys
import heapq
import bisect
import itertools

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def LI_(): return([int(x)-1 for x in sys.stdin.readline().split()])
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
    N,K = LI()
    H = LI()

    ans = 0
    for h in H:
        if h>=K:
            ans += 1
    return(ans)

if __name__ == "__main__":
    print(main())
