

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    T=I()
    M=60#60桁まで
    
    #S=1となる全ての数字が，それより後ろのS=0のもので構成できれば良い（それらを組み合わせても，S=0側も同じ組み合わせ方で対応できる）．
    #S=0のものを基底ベクトル(ぽいもの)として持っておく
    #このとき行列の標準形を構成するベクトルをイメージ
    #上位桁が等しいものがある場合，それとxorしておけば良い，これによって上位桁が同じ基底ベクトル(ぽいもの)がなくなる
    
    
    def pipo(x):
        #最上位桁が何処か
        cnt=0
        for i in range(M):
            if x==0:
                return cnt
            else:
                x=x//2
                cnt+=1
    

        
    
    for _ in range(T):
        N=I()
        A=LI()
        S=list(input())
        #後ろから見ていき，S=1の時に「S=0の数だけで作れない数」が出てきたらNG
        Vec=[]#基底管理
        flag=1#ダメなら0になる
        for i in range(N-1,-1,-1):
            #print(i,S[i]) 
            if S[i]=="0":

                now=A[i]
                p=pipo(A[i])
                for v in Vec:
                    if v[1]==p:
                        now=now^v[0]
                        p=pipo(now)
                if now!=0:
                    Vec.append((now,pipo(now)))
                    Vec.sort(reverse=True)
                            
                
            else:
                #print(Vec)
                now=A[i]
                for v in Vec:
                    if v[1]==pipo(now):
                        now=now^v[0]
                if now!=0:
                    flag=0

                    
                
        if flag:
            print(0)
        else:
            print(1)
            
            
        
        
        
        

main()
