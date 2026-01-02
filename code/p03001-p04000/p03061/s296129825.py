def main():
    import sys
    input = sys.stdin.readline
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    def query(p,q):
        p += num
        q += num
        res=0
        while p<q:
            if q&1:
                q-=1
                res=gcd(res,data[q-1])
            if p&1:
                res=gcd(res,data[p-1])
                p+=1
            p = p//2
            q = q//2
        return res

    n = int(input())
    a = tuple(map(int,input().split()))
    num =2**(n-1).bit_length()
    data=[0]*2*num

    for i in range(n):
        data[i+num-1]=a[i]
    
    for i in range(num-2,-1,-1) :
        data[i]=gcd(data[2*i+1],data[2*i+2]) 

    ans = -1
    for i in range(n):
        ans = max(ans,gcd(query(0,i),query(i+1,n)))
    print(ans)
if __name__=='__main__':
    main()