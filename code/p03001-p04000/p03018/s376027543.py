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
    
    ca = 0
    ans = 0
    i = 0
    while i<N:
        if s[i] == "A":
            ca += 1
            i += 1
        elif i<N-1 and s[i:i+2] == "BC":
            ans += ca
            i += 2
        else:
            ca = 0
            i += 1
    return(ans)
    





if __name__ == "__main__":
    print(main())
