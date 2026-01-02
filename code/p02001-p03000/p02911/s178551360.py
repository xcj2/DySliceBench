import sys
import heapq
import bisect

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return((list(sys.stdin.readline()))[:-1])
def IR(n): return([I() for _ in range(n)])

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return a * b // GCD(a,b)

def main():
    N,K,Q = LI()
    A = IR(Q)

    point = [K-Q for _ in range(N)]
    for a in A:
        point[a-1] += 1

    for p in point:
        if p>0:
            print("Yes")
        else:
            print("No")
            


if __name__ == "__main__":
    main()
