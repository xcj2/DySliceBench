import math
import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
n=I()
ls=sorted(LI(),reverse=True)
trans=0
for i in range(n-2):
    answer=0
    for j in range(i+1,n-1):
        l1=ls[i]
        l2=ls[j]
        l,r = j,n
#あえて左右一つ分ずつ広く取る
        while l+1 < r:
#この条件で探索の終点がうまく定められる
            mid = (l+r)//2
            if l1<l2+ls[mid]:
                l = mid
            else:
                r = mid
        ansij=l-j
        #print(ansij)
        answer+=ansij
    trans+=answer
print(trans)