import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))



def main():
    mod=10**9+7
    N=I()
    S=input()
    Q=I()
    
    #####segfunc######

    #評価関数
    def segfunc(x,y):
        return x|y


    #初期化
    def init(init_val):
        #init_valは操作する数列
        for i in range(N):
            seg[i+num-1]=set([ord(init_val[i])])    
        #built
        for i in range(num-2,-1,-1) :
            seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
            

    #k番目の値をxに更新
    def update(k,x):
        k += num-1
        seg[k] = x
        while k:
            k = (k-1)//2
            seg[k] = segfunc(seg[k*2+1],seg[k*2+2])

            
    #[p,q)の区間に対するクエリへの応答
    def query(p,q):
        if q<=p:
            return ide_ele
        p += num-1
        q += num-2
        res=ide_ele
        while q-p>1:
            if p&1 == 0:
                res = segfunc(res,seg[p])
            if q&1 == 1:
                res = segfunc(res,seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = segfunc(res,seg[p])
        else:
            res = segfunc(segfunc(res,seg[p]),seg[q])
        return len(res)


    #####単位元######
    ide_ele = set([])

     #num:n以上の最小の2のべき乗
    num =2**(N-1).bit_length()
    seg=[ide_ele]*2*num
    init(S)



    
    for i in range(Q):
        q,a,b=input().split()
        if q=="1":
            update(int(a)-1,set([ord(b)]))
        else:
            print(query(int(a)-1,int(b)))
            
    
    

main()
