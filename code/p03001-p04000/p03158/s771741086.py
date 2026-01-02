import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,Q=MI()
    A=LI()
    if N%2==1:#長さが奇数なら0を足しておく
        A+=[0]
        N+=1
    A.sort()
    
    """
    連続する区間or交互
    """
    
    S=[0]*(N+1)
    S2=[0]*(N+1)#偶数のみ
    
    for i in range(N):
        S[i+1]=S[i]+A[i]
        
    for i in range(0,N-1):
        S2[i+2]=S2[i]+A[i]
        
    # print(S)
    # print(S2)
        
    def calc(P):
        # 先手が上からP枚，後手がその後のP枚をとり，残りを交互に取った時の先手のscore
        fi=S[-1]-S[-P-1]
        fi+=S2[-2*P]
        return fi
    
    def ch(X,P):
        #xが指定され，先手が上からP枚以上取れるか
        maxa=A[-P-1]#後手が取るmax
        mina=A[-2*P+1]#後手がP-1ターン目までに取る取るmin(後手がPターン目に取るものはなんでも良い)
        diff=A[-P]-X
        
        # print(X,P,mina,maxa,diff)
        if diff<0:
            return False
        if X-diff<=mina and maxa<=X+diff:
            return True
        return False
        
    
    for _ in range(Q):
        x=I()
        
        #先手が上から何枚以上取れるか
        ng=N//2 +1
        ok=1#先手が最大値をとる
        while ng-ok>1:
            med=(ok+ng)//2
            if ch(x,med):
                ok=med
            else:
                ng=med
                
        # print(ok)
        print(calc(ok))
            

main()
