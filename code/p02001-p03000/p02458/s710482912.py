import bisect

S=[]

def insert(S,count,x):
    y=bisect.bisect(S,x)
    S.insert(y,x)
    count+=1
    print(count)
    return S,count

def find(S,x):
    y0=bisect.bisect_left(S,x)
    y1=bisect.bisect_right(S,x)
    return y0,y1

def erase(S,count,x):
    y0,y1=find(S,x)
    if y1-y0>0:
        del S[y0:y1]
        count-=y1-y0
    return S,count

def dump(S,L,R):
    s=bisect.bisect_left(S,L)
    e=bisect.bisect_right(S,R)
    if e-s>0:
        print('\n'.join(map(str,S[s:e])))

q=int(input())
count=0
for i in range(q):
    query=list(map(int,input().split()))
    
    if query[0]==0:
        S,count=insert(S,count,query[1])
    elif query[0]==1:
        y0,y1=find(S,query[1])
        print(y1-y0)
    elif query[0]==2:
        S,count=erase(S,count,query[1])
    else:
        dump(S,query[1],query[2])

