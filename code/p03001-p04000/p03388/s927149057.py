q = int(input())

def f(A,B,x):
    return x*B//(x+A) + 1
def F(A,B):
    st = 1
    ed = B-A-1
    gap = B-A
    maxst = 1
    while st<ed:
        bar = (st+ed)//2
        if f(A,B,bar) + bar <=gap:
            maxst = max(maxst,bar)
            st = bar + 1
        else:
            ed = bar - 1
    if f(A,B,st) + st<=gap:
        maxst = max(maxst,st)
    if f(A,B,maxst)+maxst > gap:
        return -1
    return maxst  
def solveAB(A,B):
    res = 0
    res += (A-1)*2
    st = F(A,B)
    #print(st)
    if st == -1:
        if B-A <2:
            return res
        else:
            return res+1
    if f(A,B,st)+st == B-A and (st-1)*2+1 == B-A-1:
        #print("odd and full")
        res += (st-1)*2+1
    elif f(A,B,st)+st < B-A and st*2 == B-A-1:
        #print("even and full")
        res += st*2
    elif f(A,B,st)+st < B-A and st*2 < B-A-1: 
        #print("even not full")
        res += st*2 + 1
    elif f(A,B,st)+st == B-A and (st-1)*2+1 <B-A-1:
        #print("odd not full")
        res += (st-1)*2+1+1
    return res 
     

for _ in range(q):
    a,b = map(int,input().split())
    A = min(a,b)
    B = max(a,b)
    print(solveAB(A,B))
