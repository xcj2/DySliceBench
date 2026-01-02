import sys,collections
sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
A,B,C = sorted(Is()),sorted(Is()),sorted(Is())

Bs = [0]*N
b,j = 0,0
for i in range(N):
    while j < N:
        if B[i] >= C[j]:
            b += 1
        else:
            Bs[i] = N - b
            break
        if j == N-1:
            Bs[i] = N - b
        j += 1

all = sum(Bs)
ans,sum,j = 0,0,0
for i in range(N):
    while j < N:
        if A[i] >= B[j]:
            sum += Bs[j]
        else:
            ans += all - sum
            break
        if j == N-1:
            ans += all - sum
        j += 1
print(ans)
