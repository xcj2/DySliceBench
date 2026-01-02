#8:47
MOD=10**9+7
INT_MAX=10**20+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [False for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
#################################################################################
n=int(input())
A=INPUT()
C=LIST_1D_ARRAY(10**6+1)
count=[0]*(10**6+1)
for i in range(n):
    C[A[i]]=True
    count[A[i]]+=1
for i in range(1,10**6+1):
    if C[i]==True:
        for j in range(2*i,10**6+1,i):
            C[j]=False
ans=0
for i in range(1,10**6+1):
    if C[i]==True and count[i]==1:
        ans+=1
print(ans)
