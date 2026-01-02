import bisect

S=[]

def insert(S,count,x):
    y=bisect.bisect_left(S,x)
    if y>=count or S[y]!=x:
        S.insert(y,x)
        count+=1
    print(count)
    return S,count

def find(S,x):
    y=bisect.bisect_left(S,x)
    if y<count and S[y]==x:
        judge=1
    else:
        judge=0
    return judge,y

def erase(S,count,x):
    judge,y=find(S,x)
    if judge==1:
        S.pop(y)
        count-=1
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
        print(find(S,query[1])[0])
    elif query[0]==2:
        S,count=erase(S,count,query[1])
    else:
        dump(S,query[1],query[2])

