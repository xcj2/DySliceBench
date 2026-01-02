import numpy as np
ans=[0]*9
A=[0]*3
answer=0
for i in range(3):
    A[i]=list(map(int,input().split()))
N=int(input())
b=[0]*N
for j in range(N):
    b[j]=int(input())
def checkyoko(card):
    a=0
    for k in range(3):
        if card[k]==[1,1,1]:
            a=1
    return a
def checktate(card):
    a=0
    for l in range(3):
        if [card[0][l],card[1][l],card[2][l]]==[1,1,1]:
            a=1
    return a
def nanamecheck(card):
    a=0
    if [card[0][0],card[1][1],card[2][2]]==[1,1,1] or [card[0][2],card[1][1],card[2][0]]==[1,1,1]:
        a=1
    return a
counter=0
for m in range(3):
    for n in range(3):
        if A[m][n]in b:
            ans[counter]=1
        counter+=1
ans=np.array(ans)
ans=ans.reshape(3,3)
ans=ans.tolist()
answer=(checktate(ans)==1 or checkyoko(ans)==1 or nanamecheck(ans)==1)

if answer:
    print('Yes')
else:
    print('No')