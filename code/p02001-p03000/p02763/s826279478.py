class SegmentTree():

    def __init__(self,init_val,n): #init_valは長さnの配列 O(2*n)
        self.n=n
        self.ide_ele=0
        self.num=pow(2,n-1).bit_length() #n以上の最小の2のべき乗
        self.seg=[self.ide_ele]*2*self.num #セグメントツリー本体
        
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i] 
        
        for i in range(self.num-2,-1,-1):
            self.seg[i]=(self.seg[2*i+1])|(self.seg[2*i+2])        
        
      
    def update(self,k,x): #k番目の要素をxに変更する O(logN)
        k+=self.num-1
        self.seg[k]=x
        while k:
            k=(k-1)//2
            self.seg[k]=(self.seg[2*k+1])|(self.seg[2*k+2])
    
    def query(self,p,q): #[p,q)のクエリに答える O(logN)
        if q<=p:
            return self.ide_ele

        p+=self.num-1
        q+=self.num-2
        res=self.ide_ele

        while q-p>1:

            if (p&1)==0:
                res|=self.seg[p]

            if (q&1)==1:
                res|=self.seg[q]
                q-=1
            p//=2
            q=(q-1)//2
        
        if p==q:
            res|=self.seg[p]
        else:
            res=(res|self.seg[p])|self.seg[q]
        
        return bin(res).count('1')

def main():
    n=int(input())
    s=input()

    dic={i:j for i,j in zip('abcdefghijklmnopqrstuvwxyz',[2**i for i in range(26)])}
    l=[0]*n

    for i in range(n):
        l[i]=dic[s[i]]

    st=SegmentTree(l,n)
    
    q=int(input())
    for _ in range(q):
        a=list(map(str,input().split()))
        a[0]=int(a[0])

        if a[0]==1:
            a[1]=int(a[1])
            st.update(a[1]-1,dic[a[2]])
        
        else:
            a[1]=int(a[1])-1
            a[2]=int(a[2])
            print(st.query(a[1],a[2]))
            
if __name__=='__main__':
    main()