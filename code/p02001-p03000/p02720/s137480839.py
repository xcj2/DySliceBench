def lower(upper):
    if upper==9:
        return [8,9]
    elif upper==0:
        return [0,1]
    else:
        return [upper-1,upper,upper+1]

def numerize(a):
    return sum([a[i]*(10**i) for i in range(len(a))])

def getRunruns(digit):
    if digit==1:
        return [(i,) for i in range(10)]
    elif digit==2:
        return [(k,i) for i in range(1,10) for k in lower(i)]
    else:
        runruns=getRunruns(2)
        for i in range(digit-2):
            runruns=[(k,)+i for i in runruns for k in lower(i[0])]
        return runruns

A1=[(i,) for i in range(10)]
A2=[(k,i) for i in range(1,10) for k in lower(i)]
A=A1+A2
Aprev=A2
K=int(input())
while len(A)<K+1:
    Aprev=[(k,)+i for i in Aprev for k in lower(i[0])]
    A+=Aprev
print(numerize(A[K]))
