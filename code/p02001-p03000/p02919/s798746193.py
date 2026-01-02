import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A = [a-1 for a in A]
AINV=[0]*N

for i,x in enumerate(A):
    AINV[x]=i

ANS = 0

# BIT(BIT-indexed tree)

LEN=N# 必要なら座標圧縮する

BIT=[0]*(LEN+1)# 1-indexedなtree

def update(v,w):# index vにwを加える
    while v<=LEN:
        BIT[v]+=w
        v+=(v&(-v))# 自分を含む大きなノードへ. たとえばv=3→v=4

def getvalue(v):# [1,v]の区間の和を求める
    ANS=0
    while v!=0:
        ANS+=BIT[v]
        v-=(v&(-v))# 自分より小さい2ベキのノードへ. たとえばv=3→v=2へ
    return ANS

update(AINV[-1]+1,1)

ANS=0

def search(score):
    if score<=0:
        return 0
    if score>getvalue(N):
        return N+1

    MIN=1
    MAX=N

    while MIN!=MAX:
        x=(MIN+MAX)//2

        if getvalue(x)>=score:
            MAX=x
        else:
            MIN=x+1

    return MIN
            

for i in range(N-2,-1,-1):
    update(AINV[i]+1,1)

    sc=getvalue(AINV[i]+1)


    ANS+=(i+1)*((search(sc)-search(sc-1))*(search(sc+2)-search(sc+1))+(search(sc-1)-search(sc-2))*(search(sc+1)-search(sc)))


print(ANS)