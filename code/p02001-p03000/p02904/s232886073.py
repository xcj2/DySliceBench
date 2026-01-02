n,k = map(int,input().split())
raw = list(map(int,input().split()))
num = 2**(n-1).bit_length()
seg1 = [0]*2*num
seg2 = [n]*2*num

def build(raw):
    for i in range(n):
        seg1[i+num-1] = raw[i]
        seg2[i+num-1] = raw[i]
    for i in range(num-2,-1,-1):
        seg1[i] = max(seg1[2*i+1],seg1[2*i+2])
        seg2[i] = min(seg2[2*i+1],seg2[2*i+2])
    return True

build(raw)
cnt = n-k+1

def query(seg,ele,segf,p,q):
    if q <= p:
        return False
    p += num - 1
    q += num - 2
    res = ele
    while q-p > 1:
        if not p%2:
            res = segf(res,seg[p])
        if q%2:
            res = segf(res,seg[q])
            q -= 1
        p //= 2
        q = (q-1)//2
    if p == q:
        res = segf(res,seg[p])
    else:
        res = segf(res,seg[p],seg[q])
    return res

def check(i):
    #print(i,query(seg1,0,max,i,i+k+1),query(seg2,n+1,min,i,i+k+1))
    return query(seg1,0,max,i,i+k+1) == raw[i+k] and query(seg2,n+1,min,i,i+k+1) == raw[i]

t = [0]*n
f = -1
c = -1
for i in range(n):
    if raw[i] > c:
        f += 1
    else:
        f = 0
    c = raw[i]
    t[i] = f

c2 = -1
for i in range(n-k):
    if t[i+k-1] - t[i] == k-1:
        c2 += 1
    elif check(i):
        cnt -= 1
if t[n-1] - t[n-k] == k-1:
    c2 += 1
if c2 >= 0:
    cnt -= c2
print(cnt)