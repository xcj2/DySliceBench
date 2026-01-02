INT_MAX=10**11+7
MOD=10**9+7
def INPUT():return list(float(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
import math
#=======================================================================
n=int(input())
def calc(x):
    a=0
    return int((math.sqrt(1+8*x)-1)/2)
def primefactorisation(n):
	P=[]
	while(n%2==0):
		P.append(2)
		n//=2
	i=3
	while(i<=int(math.sqrt(n))):
		while(n%i==0):
			P.append(i)
			n//=i
		i+=2
	if(n>2):
		P.append(n)
	return P
A=primefactorisation(n)
i=0
Ans=[]
while(i<len(A)):
    p=A[i]
    count=1
    i+=1
    while(i<len(A) and p==A[i]):
        count+=1
        i+=1
    Ans.append(count)
real=0
for ele in Ans:
    real+=calc(ele)
print(real)
