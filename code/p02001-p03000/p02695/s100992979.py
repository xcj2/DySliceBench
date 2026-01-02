import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

## コンテスト中に書いたコード

N, M, Q = mi()
abcd = li2(Q)

a = '0' * N
m = str(M-1)
l = [a]

while True:
    i = N-1
    while i >= 0 and a[i] == m: #更新する桁を探索
        i -= 1
    if i == -1:
        break
    a = list(a) #strのままだと書き込めないから一旦リストに変換
    num = str(int(a[i]) + 1) #更新する桁を探索
    a[i] = num
    if i != N-1:
        for j in range(i+1, N): #更新する桁が新しくなった場合、それ以降の桁の値も揃える。Ex)11199 → 11222
            a[j] = num
    tmp = ''.join(a) #文字列に戻す
    l.append(tmp)

ans = 0
for num in l:
    cnt = 0
    #num = list(map(int, list(num)))
    for i in range(Q):
        if int(num[abcd[i][1]-1]) - int(num[abcd[i][0]-1]) == abcd[i][2]:
            cnt += abcd[i][3]
    ans = max(ans, cnt)

print(ans)