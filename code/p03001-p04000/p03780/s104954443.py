def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():

    
    N,K=MI()
    a=LI()#下位の連続するn枚が不要なはず
    a.sort(reverse=True)
    #大きい方から順に足していき，K未満の最大の和を作っておく．これに対して，足してK以上になるのならそれは必要．K未満なら端しておく．
    #最終的に必要なもののうち最も小さいものがわかるはず
    
    temp=0
    ans=N
    for i in range(N):
        if temp+a[i]<K:
            temp+=a[i]
        else:
            ans=min(ans,N-i-1)
            
    print(ans)
    
    


main()
