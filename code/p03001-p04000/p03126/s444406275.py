"""#################################################################
【ABC118】
B_Foods_Loved_by_Everyone
#################################################################"""

#インポート
import sys

#入力用
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IS(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def SS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()

lst = []
cnt = 0
N, M = IS()
for i in range(N):
    lst += (LI()[1:])
for i in range(1, M+1):
    if lst.count(i) == N:
        cnt += 1
print(cnt)