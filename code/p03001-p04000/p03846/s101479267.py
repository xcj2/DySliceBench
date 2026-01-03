characteristic=10**9+7
def plus(input1,input2):
    return (input1+input1)%characteristic
def minus(input1,input2):
    return (input1-input2)%characteristic
def times(input1,input2):
    return (input1*input2)%characteristic
def exponen(input1,input2):
    binaryl=list(str(bin(input2))[2:])
    binarysize=len(binaryl)
    binarylist=[int(binaryl[binarysize-1-i]) for i in range(binarysize)]
    modlist=[0 for i in range(binarysize)]
    modlist[0]=input1
    for i in range(1,binarysize):
        modlist[i]=times(modlist[i-1],modlist[i-1])
    answer=1
    for i in range(binarysize):
        if binarylist[i]==1:
            answer=times(answer,modlist[i])
    return answer
def divide(input1,input2):
    return times(input1,exponen(input2,characteristic-2))
N=int(input())
A=sorted([int(i) for i in input().split()],reverse=True)
#6,6,4,4,2,2,0
#7,7,5,5,3,3,1,1
B=[]
for i in range(N//2):
    for p in [0,1]:
        B.append(N-1-2*i)
if N%2==1:
    B.append(0)
for i in range(N):
    if A[i]!=B[i]:
        print(0)
        exit()
print(exponen(2,N//2))
