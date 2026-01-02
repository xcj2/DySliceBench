import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
A = LI()
a = sum(A)

if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

if A[0] != 0:
    print(-1)
    exit()

B = [0]*(N+1)  #深さiの頂点数のmax
B[0] = 1

for i in range(1,N+1):
    B[i] = min(a,B[i-1]*2-A[i])
    if B[i] < 0:
        print(-1)
        exit()

ans = A[N]

r = A[N]
for i in range(N-1,-1,-1):
    ans += A[i] + min(B[i],r)
    r = A[i]+min(B[i],r)

print(ans)