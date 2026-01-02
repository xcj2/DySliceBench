import sys
sys.setrecursionlimit(10000000)
x=int(input())
A=[]
B=[]
C=[]
dictA=[-1]*x
dictB=[-1]*x
dictC=[-1]*x
for i in range(x):
    a,b,c=list(map(int,input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
def maxA(n):
    if dictA[n]!=-1:
        return dictA[n]
    if n==0:
        dictA[n]=A[0]
        return A[0]
    dictA[n]=A[n]+max(maxB(n-1),maxC(n-1))
    return dictA[n]
def maxB(n):
    if dictB[n]!=-1:
        return dictB[n]
    if n==0:
        dictB[n]=B[0]
        return B[0]
    dictB[n]=B[n]+max(maxA(n-1),maxC(n-1))
    return dictB[n]
def maxC(n):
    if dictC[n]!=-1:
        return dictC[n]
    if n==0:
        dictC[n]=C[0]
        return C[0]
    dictC[n]=C[n]+max(maxB(n-1),maxA(n-1))
    return dictC[n]
def Nmax(n):
    return max(maxA(n),maxB(n),maxC(n))
print(Nmax(x-1))