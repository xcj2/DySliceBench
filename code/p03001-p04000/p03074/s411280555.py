import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template #


N, K = mi()
strS = li()
S = [int(i) for i in strS]
S.append(0)
# S.insert(0, 1)
# print(S)

cnt = 0
lis0 = []
if S[0] == 1:
    listart = [0]
    cnt += 1
else:
    listart = []
liend = []
for i in range(1, N):
    # if S[i] == 0:
    #     cnt += 1
    if S[i-1] == 0 and S[i] == 1:
        listart.append(i)
        lis0.append(i)
    if S[i-1] == 1 and S[i] == 0:
        liend.append(i-1)
# if S[N-1] == 0:
#     lis0.append(N)
if S[N-1] == 1:
    liend.append(N - 1)
    cnt += 1
# lis.append(N)
# lis.insert(0, -1)
len0 = len(listart) + 1 - cnt
# print(listart)
# print(liend)
# print(len0)
# print(ma)
if K >= len0:
    print(N)
else:
    ma = max(liend[K - 1] + 1, N - listart[-K])
    for i in range(len(listart) - K):
        ma = max(ma, liend[i+K]-listart[i]+1)
    print(ma)
