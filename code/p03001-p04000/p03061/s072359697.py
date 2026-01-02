from sys import stdin
##  input functions for me
def ria(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##

def gcd(a, b): return b if a == 0 else gcd(b % a, a)

## main ##
N = ri()
A = ria()

L = [0] * N
R = [0] * N

L[0] = A[0]
for i in range(1, N): L[i] = gcd(A[i], L[i - 1])
R[N-1] = A[N-1]
for i in range(1, N): R[N - 1 - i] = gcd(A[N - 1 - i], R[N - 1 - i + 1])
if N > 2 : ma = max(R[1], L[N-2])
else: ma = max(A)
for i in range(1, N - 1): ma = max(ma, gcd(L[i - 1], R[i + 1]))
#print(L)
#print(R)


print(ma)





