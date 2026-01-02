import heapq
import itertools
def evaluate(siki):
    return lambda a,b,c,d:eval(siki.replace("-","-~"))%2
def changenum(siki):
    res=0
    for seq in itertools.product(range(2),repeat=4):
        a,b,c,d=seq
        if evaluate(siki)(a,b,c,d)==1:
            res+=2**(a+2*b+4*c+8*d)
    return res
D=dict()
def dget(m):
    if m in D:
        return D[m]
    else:
        return 17
q=[]
heapq.heappush(q,(1,changenum("a")))
heapq.heappush(q,(1,changenum("b")))
heapq.heappush(q,(1,changenum("c")))
heapq.heappush(q,(1,changenum("d")))
heapq.heappush(q,(1,changenum("0")))
heapq.heappush(q,(1,changenum("1")))
D[changenum("a")]=1
D[changenum("b")]=1
D[changenum("c")]=1
D[changenum("d")]=1
D[changenum("0")]=1
D[changenum("1")]=1
while(len(q)>0):
    le,n=heapq.heappop(q)
    #print(le,n,dget(240),dget(255))
    if D[n]<le:
        continue
    D[n]=min(D[n],le)
    cost=1
    if dget(65535^n)>D[n]+cost and D[n]+cost<=16:
        D[65535^n]=D[n]+cost
        heapq.heappush(q,(D[65535^n],65535^n))
    tmp=dict()
    for k in D:
        if dget(n^k)>D[n]+D[k]+3 and D[n]+D[k]+3<=16:
            tmp[n^k]=D[n]+D[k]+3
            heapq.heappush(q,(tmp[n^k],n^k))
        if dget(n&k)>D[n]+D[k]+3 and D[n]+D[k]+3<=16:
            tmp[n&k]=D[n]+D[k]+3
            heapq.heappush(q,(tmp[n&k],n&k))
    for k in tmp:
        D[k]=tmp[k]
while(True):
    S=input()
    if S==".":
        break
    print(D[changenum(S)])
