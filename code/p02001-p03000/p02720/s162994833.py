import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


K = I()

B = []

#(i, j): iから始まるj桁のルンルン数の個数
lun = {(0, 1): 1, (1, 1): 1, (2, 1): 1, (3, 1): 1, (4, 1): 1, (5, 1): 1, (6, 1): 1, (7, 1): 1, (8, 1): 1, (9, 1): 1}
for j in range(2, 11):
    for i in range(10):
        if i == 0:
            lun[(i, j)] = lun[(i, j - 1)] + lun[(i + 1, j - 1)]
        elif i == 9 :
            lun[(i, j)] = lun[(i - 1, j - 1)] + lun[(i, j - 1)]
        else:
            lun[(i, j)] = lun[(i - 1, j - 1)] + lun[(i, j - 1)] + lun[(i + 1, j - 1)]

cnt = 0
for j in range(1, 10):
    for i in range(1, 10):
        cnt += lun[(i, j)]
    B.append(cnt)

b = bisect.bisect_right(B, K)

ans = []
if b == 0:
    print(K)
    exit()
if K == B[b - 1]:
    print(pow(10, b) - 1)
    exit()
else:
    K -= B[b - 1]
    i = 1
    while K > 0:
        K -= lun[(i, b + 1)]
        i += 1
    if K == 0:
        for j in range(b + 1):
            c = i - 1 + j
            if c <= 9:
                ans.append(c)
            else:
                ans.append(9)
    else:
        K += lun[(i - 1, b + 1)]
        ans.append(i - 1)
        for l in range(b):
            if ans[-1] == 0:
                k = 0
            else:
                k = ans[-1] - 1
            while K > 0:
                K -= lun[(k, b - l)]
                k += 1
            if K == 0:
                for j in range(b - l):
                    c = k - 1 + j
                    if c <= 9:
                        ans.append(c)
                    else:
                        ans.append(9)
                break
            else:
                K += lun[(k - 1, b - l)]
                ans.append(k - 1)
print(''.join(map(str, ans)))


