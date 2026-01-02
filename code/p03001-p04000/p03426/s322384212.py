def list_1d(d,v):
    return [ v for i in range(d)]

def abs(c): 
    if c > 0: 
        return c 
    else: 
        return -c

def distance_2d(a,b):
    return(abs(a[0]-b[0])+abs(a[1]-b[1]))

h,w,d = [int(i) for i in input().split()]
sa = list_1d(h*w+1,[])
da = list_1d(h*w+1,0)
for i in range(h):
    a = [int(k) for k in input().split()]
    for j in range(w):
        sa[a[j]] = [i,j]
q = int(input())
lr = [[int(i) for i in input().split()] for i in range(q)]

for i in range(d+1,h*w+1):
    da[i] = da[i-d] + distance_2d(sa[i],sa[i-d])

for i in range(0,q):
    print(da[lr[i][1]]-da[lr[i][0]])
