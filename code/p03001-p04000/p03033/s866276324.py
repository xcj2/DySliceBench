def main():
    class segtree():
        def __init__(self,basesize):#self,モノイド,元の配列
            #ini：上限（下限）,base：元の配列,monoid：モノイド,tree：セグ木,depth：treeの深さ,
            #basesize：baseの要素数,treesize：treeの要素数,num：treesize-basesize
            
            # 初期値（上限とか下限）を決定
            self.ini=10**9+1
            #セグ木の要素数（num）および深さ（depth）を計算
            self.basesize=basesize
            self.num,self.depth=1,1
            while self.num<self.basesize:
                self.num*=2
                self.depth+=1
            self.num-=1
            #関数（モノイド、今回はmin）を設定
            self.monoid=min
            #セグ木を構築
            self.treesize=self.num+self.basesize
            self.tree=[self.ini]*self.treesize
    
        #半開区間[lower,upper)について更新の準備をする関数（テスト中、minやmaxのときのみ）
        def range_update_pre(self,lower,upper,new_value):
            q=[[0,1]]  #インデックス、階層
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
                    self.tree[i]=self.monoid(new_value,self.tree[i])
                    continue
                if k<self.treesize:
                    if lower<=kagen and chuo<=upper:self.tree[k]=self.monoid(new_value,self.tree[k])
                    elif lower<=chuo:q.append([k,f+1])
                if k+1<self.treesize:
                    if lower<=chuo and jogen<=upper:self.tree[k+1]=self.monoid(new_value,self.tree[k+1])
                    elif chuo<=upper:q.append([k+1,f+1])

        #更新
        def range_update(self):
            for i in range(1,self.treesize):
                self.tree[i]=self.monoid(self.tree[i],self.tree[(i-1)//2])
    from sys import stdin
    input=stdin.readline
    import bisect

    n,q=map(int,input().split())
    stx=[list(map(int,input().split())) for _ in [0]*n]
    d=[int(input()) for _ in [0]*q]
    stx=[[s-x,t-x-1,x] for s,t,x in stx]
    stx=[[bisect.bisect_left(d,s),bisect.bisect_right(d,t),x] for s,t,x in stx]
    seg=segtree(q)
    for s,t,x in stx:
        if s<t:
            seg.range_update_pre(s,t,x)
    seg.range_update()
    ans=[i for i in seg.tree[seg.treesize-seg.basesize:]]
    for i in ans:
        if i==10**9+1:
            print(-1)
        else:
            print(i)
main()