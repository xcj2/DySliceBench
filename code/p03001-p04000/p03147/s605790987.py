import sys 
sys.setrecursionlimit(1000)
n=int(input())
H=list(map(int,input().split()))
def bunkai(H):
    B=[]
    b=0
    f=0
    for i in range(len(H)):
        if H[i]==0:
            if i!=0:
                B.append(H[b:i-1+1])
                b=i+1
            else:
                b=i+1
        elif i==len(H)-1:
            B.append(H[b:])
    return B
def min(lis):
    min=101
    if len(lis)==0:
        return 0
    for i in range(len(lis)):
        if lis[i]<min:
            min=lis[i]
    return min
def mizu(lis,n):
    for i in range(len(lis)):
        lis[i]+=-n
    return lis
def sso(lis,sum):
    #print(sum)
    B=bunkai(lis)
    #print(B)
    if len(B)==0:
        #print("return: "+str(sum))
        return sum
    for l in B:
        #print(l)
        x=min(l)
        #print("+"+str(x))
        sum+=x
        li=mizu(l,x)
        #print("li"+str(li))
        sum=sso(li,sum)
    #print("return end:"+str(sum))
    return sum

#print(min([]))
sum=0
x=sso(H,sum)

    
print(x)
