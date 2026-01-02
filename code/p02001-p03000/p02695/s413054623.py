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

N, M, Q = mi()
abcd = li2(Q)

'''
a = '0' * N
m = str(M-1)
l = [a]

while True:
    i = N-1
    while i >= 0 and a[i] == m:
        i -= 1
    if i == -1:
        break
    a = list(a)
    num = str(int(a[i]) + 1)
    a[i] = num
    if i != N-1:
        for j in range(i+1, N):
            a[j] = num
    tmp = ''.join(a)
    l.append(tmp)
'''

def dfs(num, length):
    if length == N:
        l.append(num)
        return
    last = int(num[-1])
    for i in range(last, M):
        dfs(num + str(i), length+1)

#l = []
#dfs('0', 1)

from collections import deque
keta_list = [str(i) for i in range(M)]
l = deque([str(i) for i in range(M)])

while len(l[0]) <= N:
    num = l.popleft()
    last = int(num[-1])
    for tail in keta_list[last:]:
        l.append(num + tail)

ans = 0
for num in l:
    cnt = 0
    num = list(map(int, list(num)))
    for i in range(Q):
        if num[abcd[i][1]-1] - num[abcd[i][0]-1] == abcd[i][2]:
            cnt += abcd[i][3]
    ans = max(ans, cnt)

print(ans)