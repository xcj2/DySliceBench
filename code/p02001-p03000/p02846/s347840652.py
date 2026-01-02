import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    T=LI()
    A=LI()
    B=LI()
    
    SA=T[1]*A[1]+T[0]*A[0]
    SB=T[1]*B[1]+T[0]*B[0]
    
    if SA == SB:
        print("infinity")
    else:
        #t1+t2分後に確実にAが先行するように．
        if SB>SA:
            SB,SA=SA,SB
            A,B=B,A
        
        if A[0]>=B[0]:
            print(0)
        else:
            diff1=(B[0]-A[0])*T[0]
            diff2=SA-SB
            cnt=(diff1//diff2+1)
            ans=(cnt)*2-1
            #基本，1ループで2回，初回は0,0のため-1
            #さらに，cnt回目のループでぎり1回だけという場合があるので，その場合は1ひく
            if diff2*(cnt-1) == diff1:
                ans-=1
            print(ans)

main()
