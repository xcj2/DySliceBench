import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = MI()
P = LI()
C = LI()

for i in range(N):
    if C[i] >= 0:
        break
else:
    print(max(C))
    exit()

from itertools import accumulate


def f(A):  # Aを無限個つなげたリストの、連続K個以下の連続部分列の和の最大値
    a = len(A)
    res = 0
    if sum(A) > 0:
        if K // a > 0:
            res = sum(A) * (K // a - 1)
            r = K % a + a
        else:
            r = K % a
    else:
        r = K % a + a

    A = [0] + A + A + A
    S = list(accumulate(A))
    m = 0
    for i in range(a):
        for k in range(1, r + 1):
            b = S[i + k] - S[i]
            m = max(m, b)
    res += m
    return res


flag = [0]*N
ans = 0
for i in range(N-1):
    if flag[i] != 0:
        continue
    A = [C[i]]
    flag[i] = 1
    j = P[i]-1
    while j != i:
        A.append(C[j])
        flag[j] = 1
        j = P[j]-1
    ans = max(ans,f(A))

print(ans)
