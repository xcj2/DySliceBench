import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    
    h = map(int,input().split())
    a = map(int,input().split())
    
    def segfunc(x,y):
        return max(x,y)
        
    def init(init_val):
        for i in range(N+1):
            seg[i+num-1] = init_val[i]
        for i in range(num-2,-1,-1):
            seg[i] = max(seg[2*i+1],seg[2*i+2])
    
    def update(k,x):
        k += num-1
        seg[k] = x
        while k:
            k = (k-1)//2
            seg[k] = segfunc(seg[2*k+1],seg[2*k+2])
            
    def query(p,q):
        if q <= p:
            return ide_ele
        p += num-1
        q += num-2
        ret = ide_ele
        while q-p>1:
            if p&1 == 0:
                ret = segfunc(ret,seg[p])
            if q&1 == 1:
                ret = segfunc(ret,seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        ret = segfunc(segfunc(ret,seg[p]),seg[q])
        return ret
        
    ide_ele = 0
    num = 2**N.bit_length()
    seg = [ide_ele]*2*num

    dp = [0]*(N+1)
    
    for he,be in zip(h,a):
        tmp = query(0,he)+be
        if tmp > dp[he]:
            dp[he] = tmp
            update(he,tmp)
    
    print(query(0,N+1))

if __name__ == "__main__":
    main()
