import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
全部の山のxorを0にしたい
変化する山は2つだけ，1とどこか．
1番目の山からi番目の山に移動するものとする．
この2つの山を使って，うまく目標T（2~Nのうちi番目だけのぞいた全てのxor）を作れるか

2つの山をごちゃ混ぜにして，aとbの二つに分けるものとする
和  :S=A[0] + A[i]
xor :T

Tのbitが立っている場合，aとbの同じ位置では片方しかbitが立っていない
それ以外の場所ではaとbのbitが同じ．

j桁目のbitをxjとする，
bitの立ち方が違うとろの和は当然Tなので
bitの立ち方が同じ桁の総和を考えると
これが S-T　になるので2で割ればどのbitが立つべきかわかる 

例)
5,3,4でi=2なら
5,3をごちゃ混ぜにして，S=8でT=4を作りたい


a= x3  1  x1  x0
b= x3  0  x1  x0

2*(x3+x1+x0) = 8-4
x3 + x1 + x0 =2 
なのでx1だけ立てれば良い

---

1番目の山からしか動かせないので，このa,bが必ずしも作れるとは限らない，
a,bのうち小さい方がA[0]以下なら良い．
片方をできるだけ小さくしたいので，Tで立っているbitはどちらかに固める

"""
def main():
    mod=10**9+7
    inf = 10**13
    
    N=I()
    A=LI()
    allx=0
    for i in range(N):
        allx=allx^A[i]
        
    #　最初から後手必勝
    if allx==0:
        print(0)
        exit()
        
    #　動かせない
    if A[0]==1:
        print(-1)
        exit()
        
    ####
        
    M=45 #桁数のmaxちょい
        
    def calc(S,T):
        # SとTが与えられた状態で取れる最大のa
        # 達成可能ならそれで良いわけではない，aを最小としての計算が楽だが，実際には最小手数を求めたいので
        # aを可能な限り大きくしていきたい．(S-T)//2 部分は固定で，Tの部分だけ可変
        # 上位桁から見て，bだけbitが立っていて，aが立っていない場合，aに移していく
        
        #むり
        if T>S:
            return False
        if (S-T)%2==1:
            return False
        
        # 以下，T<S　かつ　差が偶数とする
        
        # 基本的には
        # 最小は　(S-T)//2
        # 最大が　(S-T)//2 + T
        # になるはず
        
        if T==S:
            # T=Sの場合，Tの立っているbitのうち，Tの立っているbitを割り振りたいが全てが偏るとダメ （a=0が取れないので）
            cnt=0 #　立っているbitの数，これが1だと分けられない
            m=inf #　一番小さいbitに対応する数
            T2=T
            a=0
            b=0
            for j in range(M,-1,-1):#上位桁から見て
                p=1<<j
                if p<=T2:
                    T2-=p
                    m=p
                    cnt+=1
                    if a+p<=A[0]:
                        a+=p# 可能なら足していく
                    else:
                        b+=p
                    
            if cnt==1:
                return False
            if a==0: # 何も足せなかった
                return False
            if b==0: # 全てaにたしてしまった
                a-=m # 最下位をbに譲る
            return a
        
        # aが最小のパターンでさえ，移動でaを作れん
        if (S-T)//2 > A[0]:
            return False
        
        # Tと関与しない部分の合計値=S2を先に作り，それとT部分でbitがかぶらなければOK
        T2=T
        S2=(S-T)//2
        a=S2 # S2部分は確定している
        b=S2 # S2部分は確定している
        for i in range(M,-1,-1): # 上から見ていき，
            p=1<<i
            ft=0#T2がわ
            fs=0#S2側
            if p<=T2:
                T2-=p
                ft=1
            if p<=S2:
                S2-=p
                fs=1
                
            if ft and fs:#立っているbitが被った
                return False
            
            if ft:
                if a+p<=A[0]: # 可能ならaに足す
                    a+=p
                else:
                    b+=p
                
            
        return a
    

                 
            
            
        
            

    ans=inf
    for i in range(1,N):
        S=A[0]+A[i]
        T=A[0]^A[i]^allx
        
        a=calc(S,T)
        
        if a!=0:
            # print(i,a,A[0]-a)
            ans=min(ans,A[0]-a)
            
    if ans==inf:
        ans=-1
    print(ans)
        
    
            
            
            
        
        
        
        
    
    

main()
