import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

## 3進数
'''
N = ii()

shiki = [1]
for i in range(10):
    tmp = shiki[-1]*3
    shiki.append(tmp)

ele = [3, 5, 7]
l = []
for keta in range(3, 10):
    maxx = shiki[keta]
    for i in range(maxx):
        ten = 10**(keta-1)
        tmp = 0
        for j in reversed(range(keta)):
            tmp += ele[i//shiki[j]] * ten
            i %= shiki[j]
            ten //= 10
        l.append(tmp)

cnt = 0
for num in l:
    if num > N:
        break
    num = str(num)
    if all(e in num for e in ['3', '5', '7']):
        cnt += 1
            
print(cnt)
'''

def n_shinsu(k, n):
    bi=''
    while n!=0:
        bi+=str(n%abs(k))
        if k<0:n=-(-n//k)
        else:n=n//k
    return bi[::-1]

N = ii()
maxx = 8
l = []
ele = [3, 5, 7]
for keta in range(3, 10):
    maxx = (maxx+1) * 3 - 1
    for i in range(maxx):
        tmp = n_shinsu(3, i).zfill(keta)
        ten = 1
        num = 0
        for moji in tmp[::-1]:
            num += ele[int(moji)] * ten
            ten *= 10
        l.append(num)

cnt = 0
for num in l:
    if num > N:
        break
    num = str(num)
    if all(e in num for e in ['3', '5', '7']):
        cnt += 1
            
print(cnt)