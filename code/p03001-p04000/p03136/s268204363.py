"""#################################################################
【ABC117】
B_Polygon
#################################################################"""

#インポート
import sys

#入力用
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IS(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def SS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()

N = II()
lst = sorted(LI())
if lst[-1]< sum(lst[:-1]):
    print("Yes")
else:
    print("No")