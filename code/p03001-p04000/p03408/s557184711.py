"""#################################################################
【ABC091】
B - Two Colors Card Game
#################################################################"""

#インポート
import sys

#入力用
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))  #リスト(int型)
def MI(): return map(int, sys.stdin.readline().rstrip().split())        #多変数(int型)
def II(): return int(sys.stdin.readline().rstrip())                     # 1変数(int型)
def S(): return sys.stdin.readline().rstrip()                           #文字列(str型)

N = II()
s = [S() for _ in range(N)]
M = II()
t = [S() for _ in range(M)]
max = 0
for x in set(s):
    a = s.count(x)
    b = t.count(x)
    if max < a - b:
        max = a - b
print(max)
