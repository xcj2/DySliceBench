import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
2X = ak * (2p+1)
基本的には最小公倍数/2を基本とし，これの奇数倍か．

X  = (ak//2) * (2p+1)
と書ける．第二項が奇数なので，各akが2で割り切れれう回数が同じでなければならない
a=[2,4]だと無理
"""
def main():
    from math import gcd
    N,M=MI()
    A=LI()
    
    def count(X):
        cnt=0
        while X%2==0:
            cnt+=1
            X=X//2
        return cnt
    
    C=count(A[0])
    for i in range(1,N):
        if count(A[i])!=C:
            print(0)
            exit()
            
    lca=1
    for i in range(N):
        g=gcd(lca,A[i])
        lca=(lca*A[i])//g
        
    lca2=lca//2
    ans=M//lca2 - M//lca
    
    print(ans)
    
            
    

main()
