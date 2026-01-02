from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush
from sys import stdin

mod = 1000000007

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

def main():
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]

    ini = 0
    for i in range(N):
        for j in range(N):
            if i < j and A[i] > A[j]:
                ini += 1


    diff = 0
    for i in range(N):
        for j in range(N):
            if A[i] > A[j]:
                diff += 1

    #ans = int(( 2*ini + (K-1)*diff ) * K / 2)
    ans = ((2*ini+(K-1)*diff) % (10**9+7)) * K % (10**9+7)
    ans = ans * mod_inv(2,mod) % (10**9+7)
    print(ans)

input = lambda: stdin.readline().rstrip()
main()