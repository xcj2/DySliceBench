L=input().split( )
l=len(L)
I=[0 for i in range(l)]
#構造体やクラスとしての実装を
for i in range(l):
    if str.isnumeric(L[i])==True:
        I[i]=int(L[i])
    else:
        I[i]=L[i]
S=["" for i in range(l)]

def push(M,x,top):
    top+=1
    M[top]=x
    return(M,top)


def pop(M,top):
    temp=M[top]
    M[top]=""
    top-=1
    return(M,top,temp)


def operator(a,b,x):
    if x=="+":
        return(a+b)
    elif x=="-":
        return(a-b)
    elif x=="*":
        return(a*b)

top=-1
for i in range(l):
    if str.isdigit(L[i])==True:
        top=push(S,I[i],top)[1]
        #print(S,top)
    else:
        temp1=pop(S,top)[2]
        S=pop(S,top)[0]
        top=pop(S,top)[1]
        #print(top,temp1)
        temp2=pop(S,top)[2]
        S=pop(S,top)[0]
        top=pop(S,top)[1]
        #print(top,temp2)
        #print(temp2,temp1,I[i])
        top+=1
        S[top]=operator(temp2,temp1,I[i])
        #print(S,S[top],top)
print(S[0])

