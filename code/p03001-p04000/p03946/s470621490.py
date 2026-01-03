def examD():
    N, T =LI()
    A = LI()
    maXI = [0]*N
    maXI[N-1] = A[N-1]
    for i in range(1,N):
        maXI[N-i-1] = max(maXI[N-i],A[N-i-1])
    maXAD = int(0)
    for i in range(N-1):
        maXAD = max(maXAD,maXI[i+1]-A[i])
    cur = int(0)
    for i in range(N-1):
        if maXI[i+1]-A[i]==maXAD:
            cur +=1
    print(cur)



import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
