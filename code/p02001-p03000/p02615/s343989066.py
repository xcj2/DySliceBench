import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
A = LI()

A = sorted(A,reverse=True)

a = (N-1)//2

b = 0
for i in range(a+1):
    b += A[i]


if N % 2 == 1:
    print(2*b-A[0]-A[a])
else:
    print(2*b-A[0])