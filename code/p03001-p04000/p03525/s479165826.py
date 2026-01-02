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
    D = LI()

    pigeon = [0] * 13

    for d in D:
        pigeon[d] += 1

    if pigeon[0] >= 1:
        return 0
    if pigeon[12] >=2:
        return 0
    for i in range(1,12):
        if pigeon[i] >= 3:
            return 0

    if N > 11:
        return 1

    Time = [[0,24] for _ in range(2**N)]

    ans = 0
    for x in range(2**N):
        for i in range(N):
            if (x>>i)%2:
                Time[x].append(D[i])
            else:
                Time[x].append(24-D[i])
        Time[x].sort()
        ans = max(ans,min([a-b for a,b in zip(Time[x][1:],Time[x][:-1])]))

    return(ans)

if __name__ == "__main__":
    print(main())
