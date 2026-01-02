import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
f(T)=iなるTの通り数を数えるか，
f(T)=1がN通り，f(T)=Nはいっぱい．上下左右それぞれのmaxを選び，中のものがm個であるとき2^m通り
x座標，y座標が全て相異なるのが嬉しいかも，でも，これめんどくさすぎる

ある1つの点が与える寄与を考える，

その頂点をTに含む場合＝＞必ず+1 * 2^(N-1)通り

その頂点をTに含まない場合
（右上から1つ以上，左下から1つ以上），（右下から1つ以上，左上から1つ以上）の組なら加算
これらの組みは重複しそうなので，うまく被らないように選ぶ必要あり
（右上，左下，左上0，右下0），（右上，左下，左上，右下0），（右上，左下，左上0，右下）みたいに分けて考える．

でも，各頂点ごとに４つの方向それぞれの頂点数を持つのがまず難しい．
頂点を左から順に走査．左にある頂点の個数を上下別に見ていく．
(左上，左下)を考える．
一番左なら(0,0)，次のものは(0,1) or (1,0)みたいな．見た頂点のy座標(座圧したもの)をsegTreeで管理すれば，上下の個数がそれぞれわかる．

終わったら右からもやれば4方向それぞれの個数が分かりそう．
"""
def main():
    mod=998244353
    class SegTree:
        def __init__(self,N,ide,segfunc=min):
            self.ide_ele = ide
            """
            ex)
             最小値のセグ木 → +inf
              和のセグ木 → 0
              積のセグ木 → 1
              gcdのセグ木 → 0
            """
            
            self.segfunc=segfunc
            
            #num:N以上の最小の2のべき乗
            self.num =2**(N-1).bit_length()
            self.seg=[self.ide_ele]*2*self.num

        #リストで初期化する
        def setL(self,init_val):
            #init_valは操作する数列
            for i in range(self.num):
                self.seg[i+self.num-1]=init_val[i]    
            #built
            for i in range(self.num-2,-1,-1) :
                self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 


        #k番目の値をxに更新
        def update(self,k,x):
            k += self.num-1
            self.seg[k] = x
            while k:
                k = (k-1)//2
                self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])


        #[p,q)の区間に対するクエリへの応答
        def query(self,p,q):
            if q<=p:
                return self.ide_ele
            p += self.num-1
            q += self.num-2
            res=self.ide_ele
            while q-p>1:
                if p&1 == 0:
                    res = self.segfunc(res,self.seg[p])
                if q&1 == 1:
                    res = self.segfunc(res,self.seg[q])
                    q -= 1
                p = p//2
                q = (q-1)//2
            if p == q:
                res = self.segfunc(res,self.seg[p])
            else:
                res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
            return res
    N=I()
    Y=[0]*N
    from collections import defaultdict
    ddy = defaultdict(int)
    
    L=[[0,0,0]for _ in range(N)]#x,y,i
    for i in range(N):
        x,y=MI()
        Y[i]=y
        L[i]=[x,y,i]
        
    #座圧
    Y.sort()
    for i in range(N):
        ddy[Y[i]]=i
    
    #2べき持っておく
    POW=[1]
    for i in range(N+5):
        p=(POW[-1]*2)%mod
        POW.append(p)
    
    cnt=[[0,0,0,0]for _ in range(N)]# lu,ld,ru,rd
    
    #左から見る
    L.sort()
    # print(L)
    seg=SegTree(N,0,lambda a,b: a+b)
    for j in range(N):#j個すでに見た
        i=L[j][2]#番号iの頂点
        y=L[j][1]
        yy=ddy[y]
        temp=seg.query(yy,N)#上側の個数
        cnt[i][0]=temp
        cnt[i][1]=j-temp
        # print(j,i,yy,temp)
        seg.update(yy,1)
        
    #右から見る
    seg=SegTree(N,0,lambda a,b: a+b)
    for j in range(N):#j個すでに見た
        i=L[-1-j][2]#番号iの頂点
        y=L[-1-j][1]
        yy=ddy[y]
        temp=seg.query(yy,N)#上側の個数
        cnt[i][2]=temp
        cnt[i][3]=j-temp
        seg.update(yy,1)
        
    def calc(cnt_item):
        # 引数：lu,ld,ru,rdの個数
        lu,ld,ru,rd=cnt_item
        
        temp=POW[N-1]#自身がTにある場合，周りはなんでもOK
        
        #自身がTにない場合
        
        #oxxo
        temp+=((POW[lu]-1) * (POW[rd]-1))%mod
        #xoox
        temp+=((POW[ld]-1) * (POW[ru]-1))%mod
        
        #ooox
        temp+=((POW[lu]-1) * (POW[ld]-1) *  (POW[ru]-1))%mod
        #ooxo
        temp+=((POW[lu]-1) * (POW[ld]-1) * (POW[rd]-1))%mod
        #oxoo
        temp+=((POW[lu]-1) *  (POW[ru]-1) * (POW[rd]-1))%mod
        #xooo
        temp+=((POW[ld]-1) *  (POW[ru]-1) * (POW[rd]-1))%mod
        
        #oooo
        temp+=((POW[lu]-1) * (POW[ld]-1) *  (POW[ru]-1) * (POW[rd]-1))%mod
        
        temp%=mod
        
        # print(cnt_item,temp)
        return temp
    
    ans=0
    for i in range(N):
        # print(i)
        ans=(ans+calc(cnt[i]))%mod
        
    print(ans)




main()
