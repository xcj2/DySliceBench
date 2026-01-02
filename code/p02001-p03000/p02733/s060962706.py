import sys
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def MAP(): return map(int, input().split())
inf = sys.maxsize

h, w, k = MAP()
s = [[int(i) for i in STR()] for _ in range(h)]

ans = inf
for i in range(2 ** (h - 1)): #縦方向の割り方を全探索 O(500)
    hdiv = [1 for _ in range(h)]
    for j in range(h - 1):
        tmp = 2 ** j
        hdiv[j] = 1 if i & tmp else 0
    sh = sum(hdiv)
    tmpans = sh - 1
    wdiv = [0 for _ in range(w - 1)]
    partsum = [0 for _ in range(sh + 1)]
    j = 0
    cnt = 0
    while j < w: #O(2 * 10 ** 4)
        tmp = 0
        idx = 0
        for kk in range(h): #O(10)
            tmp += s[kk][j]
            if hdiv[kk]:
                partsum[idx] += tmp
                tmp = 0
                idx += 1
        flag = True
        for kk in range(sh + 1):
            if partsum[kk] > k:
                tmpans += 1
                partsum = [0 for _ in range(sh + 1)]
                flag = False
        if flag:
            j += 1
            cnt = 0
        else:
            cnt += 1
        if cnt > 2:
            tmpans = inf
            break
    ans = min(ans, tmpans)
print(ans)
