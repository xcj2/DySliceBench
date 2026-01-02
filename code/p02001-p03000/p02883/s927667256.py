import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
コストが低い人が食べにくいものを食べる．
コストが低い人を追い抜かすことはない，（追い抜かすなら入れ替えて良いから）


"""
def main():
    mod=10**9+7
    N,K=MI()
    A=LI()
    F=LI()
    F.sort()
    A.sort(reverse=True)
    
    if K>=sum(A):
        print(0)
        exit()
        
    def ch(x):
        # x秒でクリアできるか
        temp=0#　必要修行回数
        for i in range(N):
            af=A[i]*F[i]
            if af>x:
                add=(af-x+F[i]-1)//F[i]
                temp+=(add)
                
        return temp <= K
        
    ok=10**12
    ng=0
    
    while ok-ng>1:
        med=(ok+ng)//2
        if ch(med):
            ok=med
        else:
            ng=med 
            
    print(ok)
    
main()
