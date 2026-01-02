import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    #約数列挙
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        divisors.sort(reverse=True)
        return divisors
    mod=10**9+7
    N,K=MI()
    A=LI()
    S=sum(A)
    
    div=make_divisors(S)
    N2=len(div)
    
    ans=1
    for g in div:
        L=[0]*N
        for i in range(N):#とりあえず，マイナス分だけ考えて，全部gの倍数に寄せる
            diff=A[i]%g
            L[i]=diff
        S=sum(L)
        L.sort(reverse=True)
        
        #ここから足していく
        cost=0#かかった手数
        ii=0#Lの大きい順に見ていく
        while S!=0:#プラスとマイナスで合計が0になるようにする
            b=g-L[ii]
            cost+=b
            S-=g#g*1だけ合計値をあげたから
            ii+=1
        # print(g,L,cost)
            
        if cost<=K:
            ans=g
            break
        
    print(ans)

    
    
    

main()
