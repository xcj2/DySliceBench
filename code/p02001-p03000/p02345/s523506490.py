answer=[]
D=[]
def initRMQ(nn):
    global n
    n = 1
    while n < nn:
        n*=2
    for i in range(2*n-1):
        D.append(2147483647)

def update(k,a):
    k += n-1
    D[k] = a
    while k>0:
        k = (k-1)//2
        D[k] = min(D[k*2+1] , D[k*2+2])
        
def findMin(a,b):
    return query(a,b+1,0,0,n)

def query(a,b,k,l,r):
    if r <= a or b <= l:
        return 2147483647
    if a <= l and r <= b:
        return D[k]
    
    vl = query(a, b, (k*2)+1, l, (l+r)//2)
    vr = query(a, b, (k*2)+2, (l+r)//2, r)
    return min(vl,vr)


inn,q = map(int,input().split())
initRMQ(inn)
while True:
    try:
        o,x,y = map(int,input().split())
    except:
        break
    else:
        if o == 0:
            update(x,y)
        else:
            answer.append(findMin(x,y))
            
for i in range(len(answer)):
    print(answer[i]) 
