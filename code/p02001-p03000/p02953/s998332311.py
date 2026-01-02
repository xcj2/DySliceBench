import bisect,collections,copy,heapq,itertools,math,operator,string
def I(): return int(input())
def S(): return input()
def LI(): return list(map(int,input().split()))
def LS(): return list(input().split())
##################################################
N = I()
H = LI()
if N==1:
    print('Yes')
    exit()
if N==2:
    print('Yes' if H[0]-1<=H[1] else 'No')
    exit()
for i in range(N-1):
    if i==0:
        H[i] -= 1
        continue
    if H[i-1]<=H[i]-1<=H[i+1]:
        H[i] -= 1
        continue
    if H[i-1]<=H[i]<=H[i+1]:
        continue
    print('No')
    break
else:
    print('Yes')
