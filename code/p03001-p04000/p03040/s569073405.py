import sys

input=sys.stdin.readline

Q=int(input())
ques=[[] for i in range(0,Q)]
value=set([])
for i in range(0,Q):
    ques[i]=list(map(int,input().split()))
    if ques[i][0]==1:
        value.add(ques[i][1])

value=list(value)
value.sort()
n=len(value)
dic={}
for i in range(n):
    dic[value[i]]=0
    dic[value[i]]=i

#####segfunc######
def segfunc(x,y):
    return x+y

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2])

def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])

def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele =0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

index=dic[ques[0][1]]
update(index,1)
minx=ques[0][1]
minf=0
B=ques[0][2]
count=1
for i in range(1,Q):
    if ques[i][0]==2:
        print(minx,minf+B)
    else:
        a=ques[i][1]
        b=ques[i][2]
        index=dic[a]
        count+=1
        B+=b
        minf+=abs(a-minx)
        update(index,seg[index+num-1]+1)
        start=0
        end=n-1
        while end-start>1:
            test=(end+start)//2
            if query(0,test+1)>=(count+1)//2:
                end=test
            else:
                start=test

        if query(0,start+1)>=(count+1)//2:
            t=start
        else:
            t=end

        if value[t]>minx:
            if count%2==1:
                minf-=value[t]-minx
                minx=value[t]
            else:
                minf-=2*(value[t]-minx)
                minx=value[t]
        elif minx>value[t]:
            if count%2==1:
                minf-=value[t]-minx
                minx=value[t]
            else:
                minx=value[t]
