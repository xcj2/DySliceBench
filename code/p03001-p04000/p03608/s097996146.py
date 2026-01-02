import sys
import itertools

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(sys.stdin.readline()[:-1])
def IR(n): return([I() for _ in range(n)])

def main():
    N,M,R = LI()
    rs = [int(x) -1 for x in sys.stdin.readline().split()]
    D = [[10**10]*N for _ in range(N)]
    for _ in range(M):
        A,B,C = LI()
        D[A-1][B-1] = C
        D[B-1][A-1] = C
    for i in range(N):
        D[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j],D[i][k]+D[k][j])

    ans = 10**11
    for trs in itertools.permutations(rs):
        tans = 0
        for i in range(R-1):
            tans += D[trs[i]][trs[i+1]]
        ans = min(ans,tans)
    
    return(ans)

if __name__ == "__main__":
    print(main())
