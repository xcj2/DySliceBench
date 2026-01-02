def main():
    class segtree():
        def __init__(self,base,monoid,ini):#self,モノイド,元の配列
            #ini：上限（下限）,base：元の配列,monoid：モノイド,tree：セグ木,depth：treeの深さ,
            #basesize：baseの要素数,treesize：treeの要素数,num：treesize-basesize
            
            # 初期値（上限とか下限）を決定
            self.ini=ini
            #セグ木の要素数（num）および深さ（depth）を計算
            self.base=base
            self.basesize=len(self.base)
            self.num,self.depth=1,1
            while self.num<self.basesize:
                self.num*=2
                self.depth+=1
            self.num-=1
            #関数（モノイド、今回はmin）を設定
            self.monoid=monoid
            #セグ木を構築
            self.treesize=self.num+self.basesize
            self.tree=[None]*self.treesize
            #segtree[m]以降に代入したい配列を入力していく
            for i in range(self.num, self.treesize):self.tree[i]=self.base[i-self.num]
            #segtree[m]以降の情報を使って、0に向かってセグ木を構築していく
            for i in range(self.num-1,-1,-1):
                j=2*i+1
                if j>=self.treesize:self.tree[i]=self.ini
                else:self.tree[i]=self.monoid(self.tree[j],self.tree[min(j+1,self.treesize-1)])
        
        #条件を満たす(サンプルの条件はs以下になること)最大のインデックスを返す関数
        def max_index(self,index_func):
            #探していく
            i=0
            while i<self.num:
                k=2*i+1
                if k+1<self.treesize:
                    if index_func(self.tree[k+1]):
                        i=k+1
                        continue
                if k<self.treesize:
                    if index_func(self.tree[k]):
                        i=k
                        continue
                return -1
            return i-self.num
    
        #条件を満たす(サンプルの条件はs以下になること)最小のインデックスを返す関数
        def min_index(self,index_func):
            #探していく
            i=0
            while i<self.num:
                k=2*i+1
                if k<self.treesize:
                    if index_func(self.tree[k]):
                        i=k
                        continue
                if k+1<self.treesize:
                    if index_func(self.tree[k+1]):
                        i=k+1
                        continue
                return -1
            return i-self.num
    
        #半開区間[lower,upper)の最小値（とか）を探す関数
        def search(self,lower,upper):
            q=[[0,1]]  #インデックス、階層
            #返り値を初期化
            ret=self.ini
            while q:
                i,f=q.pop()
                #popしたインデックスと階層から、求める下限と上限を算出する
                #幅
                width=pow(2,self.depth-f)
                #下限と中央と上限
                kagen=(i-pow(2,f-1)+1)*width
                chuo=kagen+width//2
                jogen=kagen+width
                k=2*i+1
                if lower<=kagen and jogen<=upper:
                    ret=self.monoid(ret,self.tree[i])
                    continue
                if k<self.treesize:
                    if lower<=kagen and chuo<=upper:ret=self.monoid(ret,self.tree[k])
                    elif lower<=chuo:q.append([k,f+1])
                if k+1<self.treesize:
                    if lower<=chuo and jogen<=upper:ret=self.monoid(ret,self.tree[k+1])
                    elif chuo<=upper:q.append([k+1,f+1])
            return ret
    
        #base[i]をsに更新したときにセグ木全体を更新する関数
        def update(self,index,new_value):
            i=index+self.num
            self.tree[i]=new_value
            temp=new_value
            while i!=0:
                k=(i-1)//2
                if i%2==1:
                    temp=self.monoid(self.tree[min(i+1,self.treesize-1)],temp)
                else:
                    temp=self.monoid(self.tree[i-1],temp)
                if self.tree[k]!=temp:
                    self.tree[k]=temp
                    i=k
                    continue
                break
    
    n,m=map(int,input().split())
    lrc=[list(map(int,input().split())) for _ in [0]*m]
    lrc.sort(key=lambda x:x[1])
    t=segtree([10**15]*n,min,10**15)
    t.update(0,0)
    for l,r,c in lrc:
        t.update(r-1,min(t.search(r-1,r),t.search(l-1,n)+c))
    tt=t.search(n-1,n)
    if tt==10**15:
        print(-1)
        return 0
    print(tt)
main()