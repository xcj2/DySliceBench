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

def factorization(N):
    arr = []
    temp = N
    for i in range(2, int(-(-N**0.5//1))+1):
        if temp%i == 0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //=i
            arr.append([i,cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([N,1])

    return arr

def main():
    A,B = LI()
    GCD_AB = GCD(A,B)
    if GCD_AB == 1:
        return 1
    arr = factorization(GCD(A,B))
    return(len(arr)+1)

if __name__ == "__main__":
    print(main())
