n,k =map(int,input().split())
p = list(map(int,input().split()))

def init(init_val):
    for i in range(n):
        MI[i+num-1]=init_val[i]
        MA[i+num-1]=init_val[i]    
    for i in range(num-2,-1,-1) :
        MI[i]=min(MI[2*i+1],MI[2*i+2])
        MA[i]=max(MA[2*i+1],MA[2*i+2])
    
def update(k,x):
    k += num-1
    MI[k] = x
    MA[k] = x
    while k+1:
        k = (k-1)//2
        MI[k] = min(MI[k*2+1],MI[k*2+2])
        MA[k] = max(MA[k*2+1],MA[k*2+2])

def rangemin(p,q):
    if q<=p:
        return 1<<100
    p += num-1
    q += num-2
    res= 1<<100
    while q-p>1:
        if p&1 == 0:
            res = min(res,MI[p])
        if q&1 == 1:
            res = min(res,MI[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,MI[p])
    else:
        res = min(min(res,MI[p]),MI[q])
    return res

def rangemax(p,q):
    if q<=p:
        return -1
    p += num-1
    q += num-2
    res= -1
    while q-p>1:
        if p&1 == 0:
            res = max(res,MA[p])
        if q&1 == 1:
            res = max(res,MA[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,MA[p])
    else:
        res = max(max(res,MA[p]),MA[q])
    return res

#n:リスト長
num =2**(n-1).bit_length()
MI=[1<<100]*2*num
MA=[-1]*2*num

init(p)
a = 0
l = -1
c = 0
for i in range(1,n):
    if p[i-1] > p[i]:
        a = i
    if i >= k-1 and a <= i-k+1:
        if i-l > 1:
            c += 1
        l= i

ans = 1-max(c-1,0)

for i in range(n):
    if i >=k:
        if rangemin(i-k+1,i) < p[i-k] or rangemax(i-k+1,i) > p[i]:
            ans += 1

print(ans)