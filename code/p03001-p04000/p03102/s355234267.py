"""#################################################################
【ABC121】
B_Can_you_solve_this
#################################################################"""

#インポート
import sys

#入力用
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(input())
def S(): return input()

N, M, C = MI()
B = LI()
cnt = 0
for i in range(N):
    sum = 0
    A = LI()
    for j in range(M):
        sum += A[j] * B[j]
    if sum + C > 0:
        cnt += 1
print(cnt)