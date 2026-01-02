import sys
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

MOD = 10 ** 9 + 7
N,K = map(int,input().split())
A = np.array([input().split() for _ in range(N)],dtype=np.int64)

def mult1(A,B):
    C = np.zeros_like(A)
    for i in range(N):
        for j in range(N):
            C[i,j] = (A[i,:] * B[:,j] % MOD).sum() % MOD
    return C

def mult(A,B):
    # 桁あふれ回避のため
    M = 1 << 16
    A1,A2 = A//M,A%M
    B1,B2 = B//M,B%M
    X,Y,Z = (np.dot(P,Q) % MOD for P,Q in ((A1,B1),(A1-A2,B1-B2),(A2,B2)))
    return ((X << 32) + (X+Z-Y << 16) + Z) % MOD

def power(A,k):
    if k == 1:
        return A
    X = power(A,k//2)
    X = mult(X,X)
    return mult(A,X) if k&1 else X

answer = power(A,K).sum() % MOD
print(answer)