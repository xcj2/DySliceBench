import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,K = MI()
A = [0] + LI()

visited = [0]*(N+1)
times = [0]*(N+1)
i = 1
a = 0
visited[1] = 0
times[0] = 1
while True:
    i = A[i]
    a += 1
    if visited[i] != 0:
        times[a] = i
        b,c = visited[i],a
        break
    else:
        visited[i] = a
        times[a] = i


if K <= a:
    print(times[K])
else:
    print(times[a+(K-a)%(b-a)])
