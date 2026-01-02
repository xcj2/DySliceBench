def pushback(A,t,x):
    A[t].append(x)
    return A

def dump(A,t):
    count=len(A[t])
    if count==0:
        print()
    else:
        print(str(A[t][0]),end="")
        if count>1:
            for i in range(1,count):
                print(" "+str(A[t][i]),end="")
        print()

def clear(A,t):
    A[t].clear()
    return A

n,q=(int(x) for x in input().split())
A=[[] for i in range(n)]
for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==0:
        A=pushback(A,query[1],query[2])
    elif query[0]==1:
        dump(A,query[1])
    else:
        A=clear(A,query[1])

