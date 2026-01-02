"""#################################################################
【ABC110】
B_1_Dimensional_Worlds_Tale
#################################################################"""

#インポート
import sys

#入力用
def ILI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def ISS(): return sys.stdin.readline().rstrip().split()
def IS(): return sys.stdin.readline().rstrip()

N, M, X, Y = ISI()
x = ILI()
y = ILI()
good = False
for i in range(X+1, Y+1):
    if max(x) < i and min(y) >= i:
        good = True
        break
if good == True:
    print("No War")
else:
    print("War")