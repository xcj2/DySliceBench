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
    N,M = LI()
    XY = []
    for _ in range(M):
        XY.append(LI())

    possibility = [[False,1] for _ in range(N)]
    possibility[0] = [True,1]

    for x,y in XY:
        if possibility[x-1][0]:
            possibility[y-1][0] = True
        possibility[x-1][1] -= 1
        possibility[y-1][1] += 1

        if possibility[x-1][1] == 0:
            possibility[x-1][0] = False

    ans = 0
    for i in range(N):
        if possibility[i][0]:
            ans += 1
    return(ans)

if __name__ == "__main__":
    print(main())
