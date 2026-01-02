import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,M,K = map(int,S().split())
friend = [LI() for i in range(M)]
enemy = [LI() for i in range(K)]

from collections import deque,defaultdict,Counter

G = defaultdict(list)

for a,b in friend:
    G[a].append(b)
    G[b].append(a)

A = [0]*(N+1)  #根

for i in range(1,N+1):
    if A[i] != 0:
        continue
    else:
        A[i] = i
        q = deque([i])
        while q:
            n = q.pop()
            for j in G[n]:
                if A[j] == 0:
                    A[j] = i
                    q.append(j)

c = Counter(A)

A = [[A[i],c[A[i]]] for i in range(N+1)]  #(根,連結成分の大きさ)

#同じ連結成分の中の友達関係、敵対関係の分だけ引く

for a,b in friend:
    if A[a][0] == A[b][0]:
        A[a][1] -= 1
        A[b][1] -= 1
for c,d in enemy:
    if A[c][0] == A[d][0]:
        A[c][1] -= 1
        A[d][1] -= 1

print(*[A[i][1]-1 for i in range(1,N+1)])

#-1は自分自身