import math
INT_MAX=10**18+7
MOD=10**9+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
#################################################################################
n=int(input())
def calc(x,n):
    while(n%x==0):
        n//=x
    if n%x==1:
        return True
    else:
        return False

def factors(n):
    A=[]
    i=1
    while(i<=math.sqrt(n)):
        if n%i==0:
            if (n//i)==i:
                A.append(i)
            else:
                A.append(i)
                A.append(n//i)
        i+=1
    return A
x=len(factors(n-1))-1
#print(x)
A=factors(n)
A.sort()
#print(A)
for i in range(1,len(A)):
    if calc(A[i],n) is True:
        x+=1
print(x)
