import bisect

D=[]
N=[]
count=0

def insert(D,N,count,key,x):
    y=bisect.bisect_left(D,key)
    if y<count and D[y]==key:
        N[y]=x
    else:
        D.insert(y,key)
        N.insert(y,x)
        count+=1
    return D,N,count

def get(D,N,count,key):
    y=bisect.bisect_left(D,key)
    if y<count and D[y]==key:
        print(N[y])
    else:
        print(0)

def erase(D,N,count,key):
    y=bisect.bisect_left(D,key)
    if y<count and D[y]==key:
        D.pop(y)
        N.pop(y)
        count-=1
    return D,N,count

q=int(input())
for i in range(q):
    query=list(map(str,input().split()))
    query[0]=int(query[0])
    if query[0]==0:
        D,N,count=insert(D,N,count,query[1],int(query[2]))
    elif query[0]==1:
        get(D,N,count,query[1])
    else:
        D,N,count=erase(D,N,count,query[1])

