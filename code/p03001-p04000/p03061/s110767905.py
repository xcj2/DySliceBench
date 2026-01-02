def main():
    import sys
    input = sys.stdin.readline
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    #[p,q)のgcd
    def query(p,q):
        if p>n-1 or q<1:
            return 0
        if abs(q-p)<=1:
            return a[p]
        p += num-1
        q += num-2
        res=0
        while q>p:
            if p&1 == 0:
                res = gcd(res,seg[p])
            if q&1 == 1:
                res = gcd(res,seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        res = gcd(res,seg[p])
        return res

    n = int(input())
    a = tuple(map(int,input().split()))
    #num:n以上の最小の2のべき乗
    num =2**(n-1).bit_length()
    seg=[0]*2*num

    for i in range(n):
        seg[i+num-1]=a[i]    
    for i in range(num-2,-1,-1) :
        seg[i]=gcd(seg[2*i+1],seg[2*i+2]) 

    ans = -1
    for i in range(n):
        ans = max(ans,gcd(query(0,i),query(i+1,n)))
    print(ans)
if __name__=='__main__':
    main()