def add(a,b): 
    return a + b
def sub(a,b): 
    return a - b
def mul(a,b): 
    return a * b
def div(a,b): 
    return a/ float(b)

A=input().split()
i=0
for j in range(len(A)):
    if A[i]=="+":
        A[i-2]=(int)(A[i-2])
        A[i-1]=(int)(A[i-1])
        A[i]=add(A[i-2],A[i-1])
        r=A[i]
        del A[i-2]
        del A[i-2]
        i=i-2
    if A[i]=="-":
        A[i-2]=(int)(A[i-2])
        A[i-1]=(int)(A[i-1])
        A[i]=sub(A[i-2],A[i-1])
        r=A[i]
        del A[i-2]
        del A[i-2]
        i=i-2
    if A[i]=="*":
        A[i-2]=(int)(A[i-2])
        A[i-1]=(int)(A[i-1])
        A[i]=mul(A[i-2],A[i-1])
        r=A[i]
        del A[i-2]
        del A[i-2]
        i=i-2
    if A[i]=="/":
        A[i-2]=(int)(A[i-2])
        A[i-1]=(int)(A[i-1])
        A[i]=div(A[i-2],A[i-1])
        r=A[i]
        del A[i-2]
        del A[i-2]
        i=i-2
    i=i+1
print(r)

