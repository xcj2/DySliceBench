import bisect

M={}
D=[]

def insert(M,D,key,x):
    if key not in M:
        M[key]=[]
        bisect.insort_left(D,key)
    M[key].append(x)
    return M,D

def get(M,D,key):
    if key in M and M[key]!=[]:
        print('\n'.join(map(str,M[key])))

def erase(M,D,key):
    if key in M:
        M[key]=[]
    return M,D

def dump(M,D,L,R):
    s=bisect.bisect_left(D,L)
    e=bisect.bisect_right(D,R)
    if e-s>0:
        #ループを使わずにできる方法を考える
        for i in range(s,e):
            for j in M[D[i]]:
                print(D[i],j)

q=int(input())
for i in range(q):
    query=list(map(str,input().split()))
    query[0]=int(query[0])
    if query[0]==0:
        M,D=insert(M,D,query[1],int(query[2]))
    elif query[0]==1:
        get(M,D,query[1])
    elif query[0]==2:
        M,D=erase(M,D,query[1])
    else:
        dump(M,D,query[1],query[2])

