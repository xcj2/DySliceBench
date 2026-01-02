import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
Sは全部0と仮定して良い，最後に2^N倍
Cはソートしておく，後ろから使う．

iは0indexとする
各C[i]ごとに見るか，そうしたら，それが何番目かによって寄与が決まる
i桁目なので左にi桁あるけど，これは通り数にしか関与しない
右側にN-i-1(=aとする)桁分ある．a桁のうちj桁1があるとして，寄与がj*C[i]

通り数：
右：a個からj個えらぶ=aCj
左：0でも1でも置ける=2^i

変更時のD：j+1

i,jの2つのΣで考えると，j側は結局Σ((j+1) * aCj)
j=0~aでΣ(j+1 * aCj) = (a+2) * pow(2,a-1) = (N-i+2) * pow(2,a-1)

"""

def main():
    mod=10**9+7
    N=I()
    C=LI()
    C.sort()
    ans=0
    
    def calc(ii):
        a = N-ii-1
        if a==0:
            temp_j=1
        else:
            temp_j = (a+2) * pow(2,a-1,mod)
        temp = C[ii]*pow(2,ii,mod)*temp_j
        return temp%mod
    
    for i in range(N):
        ans=(ans+calc(i))%mod
        
    ans=(ans*pow(2,N,mod))%mod
        
    print(ans)

  

main()
