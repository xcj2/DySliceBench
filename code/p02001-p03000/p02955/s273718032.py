from collections import deque
N,K=map(int,input().split())
L=list(map(int,input().split()))

def factorization(N):
    res=[]
    for i in range(2,int(N**(1/2))+2):
        if not N%i:
            r=0
            while not N%i:
                N//=i
                r+=1
            res.append((i,r))
    if N>1:
        res.append((N,1))
    return res

def factors(n):
    res=[1]
    for i,j in factorization(n):
        res+=[r*i**(b+1) for r in res for b in range(j)]
    return res

A=factors(sum(L))
A.sort()

def check(n):
    B=deque(sorted([a%n for a in L if a%n>0]))
    rp,rm=0,0
    while B:
        if rp<rm:
            rp+=B.popleft()
        else:
            rm+=n-B.pop()
    if rp!=rm:
        return False
    return rp<=K

# ok=-1
# ng=len(A)
# print(A,[check(a) for a in A])
# while abs(ok-ng)>1:
#     mid=(ok+ng)//2
#     if check(A[mid]):
#         ok=mid
#     else:
#         ng=mid
# print(A[ok])

for a in reversed(A):
    if check(a):
        break
print(a)