"""#################################################################
【ABC119】
B - Digital Gifts
#################################################################"""

#インポート
import sys

#入力用
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def SS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()

sum = 0
N = II()
for i in range(N):
    x, y = SS()
    if y == "JPY":
        sum += float(x)
    else:
        sum += float(x)*380000
print(sum)
