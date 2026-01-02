import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
面倒なので差分を考えておく，
この差分を+ or - のどちらで使うかの2択，
合計値を0に近づけたい，
各マスごとに取れる範囲をsetで持ちながら，とやりたいが取れる範囲が多そうな気もする．

絶対値が6400を超える分は持つ必要ないな，ギリ行けるかも?
やっぱり遅いか.
dpだと遷移が遅そうだからsetにしようとしたけど，これも遅い．

dpで取れる値をいっぺんにシフトできれば高速化可能，めっちゃでかい二進数を用意する？

"""
def main():
    mod=10**9+7
    H,W=MI()
    A=[]
    B=[]
    for i in range(H):
        a=LI()
        A.append(a)
    for i in range(H):
        b=LI()
        B.append(b)
        
    AB=[[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            ab=abs(A[i][j] - B[i][j])
            AB[i][j]=ab
            
    offset = 80*(H+W) #負数があるのでbitをずらす
    
    dp=[[0]*(W+1) for _ in range(H+1)]
    
    def calc(a,d):
        # aをdだけ前後にずらす
        return (a<<d) | (a>>d) 
    
    
    dp[0][0]=1<<(offset+AB[0][0]) | 1<<(offset-AB[0][0])
    
    for i in range(H):
        for j in range(W):
            dp[i][j+1] = dp[i][j+1] | calc(dp[i][j],AB[i][j+1])
            dp[i+1][j] = dp[i+1][j] | calc(dp[i][j],AB[i+1][j])

    
    a=dp[-2][-2]
    
    # 正負で対称なので片側だけで良い
    a=a>>offset # ずらしたぶん戻す
    for i in range(offset):
        if a>>i & 1:
            print(i)
            break
        
    # for i in range(H):
    #     for j in range(W):
    #         print(bin(dp[i][j]>>offset))
    #         # print(bin(dp[i][j]))
    #         print()
    
    
        
                    
                
    

main()
