#ABC129-C
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
n,m=IL()
D=[True]*n
for i in range(m):
    D[I()-1]=False
A=[0]*n
if n==1:
    if D[0]:
        print(1)
    else:
        print(0)

else:
    if D[0]:
        A[0]=1
        if D[1]:
            A[1]=2
        else:
            A[1]=0
    else:
        A[0]=0
        if D[1]:
            A[1]=1
        else:
            A[1]=0
    for i in range(2,n):
        if D[i]:
            A[i]=A[i-1]+A[i-2]
        else:
            A[i]=0
    print(A[n-1]%1000000007)