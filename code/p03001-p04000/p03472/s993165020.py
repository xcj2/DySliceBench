import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
 
import bisect
 
 
N, H = mi()
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = mi()
 
B = sorted(B)
a = max(A)
m = bisect.bisect_left(B, a)
'''
s = 1
e = N
m = (s+e)//2
pre_m = 0
while True:
    m = (s+e)//2
    if B[m-1] > a:
        e = m
    elif B[m-1] <= a:
        s = m
    if s==e:
        m -= 1
        break
    #else:
        #break
    if e-s==1 and pre_m==m:
        break
    pre_m = m
'''
rem = H - sum(B[m:])
if rem > 0:
    print((N-m)+rem//a+(rem%a!=0))
else:
    for i in range(m, N):
        rem += B[i]
        if rem>0:
            print(N-i)
            exit()