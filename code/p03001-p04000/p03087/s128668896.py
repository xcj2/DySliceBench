import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


N, Q = mi()
# print(N, Q)
S = li()
Alist = []
for i in range(N - 1):
    if S[i] == 'A' and S[i + 1] == 'C':
        Alist.append(i)
Aset = set(Alist)
AClist = [0]*(N+1)
for i in range(N-1):
    if i in Aset:
        AClist[i + 2] = AClist[i + 1] + 1
    else:
        AClist[i+2] = AClist[i+1]
        # print(AClist)

for i in range(Q):
    l, r = mi()
    if AClist[l - 1] != AClist[l]:
        print(AClist[r] - AClist[l])
    else:
        print(AClist[r] - AClist[l-1])
