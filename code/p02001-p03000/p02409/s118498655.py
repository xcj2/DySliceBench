import bisect,collections,copy,itertools,math,string
def I(): return int(input())
def S(): return input()
def LI(): return list(map(int,input().split()))
def SI(): return list(input().split())
##################################################
def main(N,bfrv):
    ans = [[[0]*10 for _ in range(3)] for _ in range(4)]
    for x in bfrv:
        b,f,r,v = x[0],x[1],x[2],x[3]
        ans[b-1][f-1][r-1] += v
    for i,x in enumerate(ans):
        if i:
            print('#'*20)
        for y in x:
            print(' ',end='')
            print(*y)
    
N = I()
bfrv = [LI() for _ in range(N)]
main(N,bfrv)
