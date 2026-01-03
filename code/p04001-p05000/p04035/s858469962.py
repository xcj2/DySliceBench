import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
逆順に見る，2つで長さL以上のものが作れればOKそうでなければ不可

最初dequeで解こうとしたけど，純粋に間違ってた
"""
def main():
    mod=10**9+7
    N,L=MI()
    A=LI()
    t=-1 #最後に外すとこ
    for i in range(N-1):
        # 結び目iを見る
        temp=A[i]+A[i+1]
        if temp >= L:
            t=i
            break
        
    if t==-1:
        print("Impossible")
    else:
        print("Possible")
        ans=[]
        for i in range(t):
            ans.append(i)
        for i in range(N-2,t,-1):
            ans.append(i)
        ans.append(t)
        
        for i in ans:
            print(i+1)
            
    
    
    

main()
