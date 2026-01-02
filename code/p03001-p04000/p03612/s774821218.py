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

def main():
    N = I()
    A = LI()
    ans = 0
    for i in range(N-1):
        if A[i] == i+1:
            ans += 1
            A[i],A[i+1] = A[i+1],A[i]

    if A[N-1] == N:
        ans += 1

    return(ans)


if __name__ == "__main__":
    print(main())
