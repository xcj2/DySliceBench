def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
count = 0
ans = "No"

N = i()
A = l()

M = 1000
S = 0
P = 0

for i in range(1,N):
    #print(A[i-1],A[i])
    #print(A[i-1] < A[i])
    if A[i-1] < A[i]:
        S += M // A[i-1]
        P = A[i-1]
        if M - S*P >= 0:
            M -= S*P
    elif A[i-1] > A[i]:
        M += S*A[i-1]
        S = 0
    #print(M,S,P)
if S > 0:
    M += S*A[N-1]
print(M)



