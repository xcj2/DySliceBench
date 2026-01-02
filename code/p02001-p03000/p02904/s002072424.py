def init(seg,init_val,n,num):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=min(seg[2*i+1],seg[2*i+2]) 
    return seg
    
def query(seg,p,q,n,num):
    if q<=p:
        return float("inf")
    p += num-1
    q += num-2
    res=float("inf")
    while q-p>1:
        if p&1 == 0:
            res = min(res,seg[p])
        if q&1 == 1:
            res = min(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,seg[p])
    else:
        res = min(min(res,seg[p]),seg[q])
    return res

def init2(seg,init_val,n,num):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i] = max(seg[2*i+1],seg[2*i+2]) 
    return seg
    
def query2(seg,p,q,n,num):
    ide_ele = -float("inf")
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg[p])
        if q&1 == 1:
            res = max(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg[p])
    else:
        res = max(max(res,seg[p]),seg[q])
    return res


def main():
    import sys
    input = sys.stdin.readline
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    
    num =2**(N-1).bit_length()
    seg1=[float("inf")]*2*num
    seg1 = init(seg1,P,N,num)
    seg2=[-float("inf")]*2*num
    seg2 = init2(seg2,P,N,num)
    
    ans = 1
    c = 0
    tmp = 0
    for i in range(N-1):
        if P[i]<P[i+1]:
            tmp += 1
        else:
            if tmp >= K-1:
                c += 1
            tmp = 0
    if tmp >= K-1:
        c += 1
        tmp = 0
        
        
    for i in range(N-K):
        m = query(seg1, i, i+K+1,N,num)
        M = query2(seg2, i, i+K+1,N,num)
        if P[i]!=m or P[i+K]!=M:
            ans += 1
    
    print(ans- max(0,c-1))
        
    
    
main()