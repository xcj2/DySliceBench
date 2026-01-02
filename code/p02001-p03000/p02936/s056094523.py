import sys
sys.setrecursionlimit(10000000)
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

N, Q = LI()
P = [0] * N
V = [[] for _ in range(N)]

w = [0]*N
for i in range(N-1):
    A, B = LI()
    V[A-1].append(B-1)
    V[B-1].append(A-1)
#    AB[i] = LI()
for i in range(Q):
    p, x = LI()
    P[p-1] += x

#print(V)
for i in range(N):
    w[i] += P[i]

#i = int(0)
#for l in V:
#   for j in l:
#        print(i, j)
#        w[j] += w[i]
#        print(w)
#    i +=1
def solve(v,i):
#    print(v,i)
#    print(w)
#    print("#####")
    if not v[i]:
        return
    else:
        for l in v[i]:
            w[l] += w[i]
            v[l].remove(i)
            solve(v,l)
        return
i =int(0)
solve(V,i)

print(" ".join(map(str,w)))
