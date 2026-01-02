import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N=I()
P=LS()
Q=LS()

l = ["".join([str(n) for n in list(i)]) for i in itertools.permutations(range(1,N+1),N)]

ans = abs(l.index("".join(P)) - l.index("".join(Q)))
print(ans)
