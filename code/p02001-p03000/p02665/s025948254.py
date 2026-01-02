import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))
n=n_in()
A=l_in()

if n == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()


if A[0] != 0:
    print(-1)
    exit()
    
B=[0]*(n+1)
B[0] = 1

upper = max(A)

S=[0]*(n+1)
S[0] = A[0]

for i in range(1,n+1):
    S[i] = S[i-1]+A[i]



for i in range(1, n):
    B[i] = min(B[i-1]*2-A[i], S[n]-S[i])
    if B[i] <= 0:
        print(-1)
        exit()

if A[n] > B[n-1]*2:
    print(-1)
    exit()
        
print(sum(A)+sum(B))
    
