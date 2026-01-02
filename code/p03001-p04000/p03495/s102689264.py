"""#################################################################
【ABC081】
C - Not so Diverse
#################################################################"""

#インポート
import sys
from collections import Counter

#入力用
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))  #リスト(int型)
def MI(): return map(int, sys.stdin.readline().rstrip().split())        #多変数(int型)
def II(): return int(sys.stdin.readline().rstrip())                     # 1変数(int型)
def S(): return sys.stdin.readline().rstrip()                           #文字列(str型)

N, K = MI()
A = LI()
A = sorted(Counter(A).values(), reverse = True)
sum = sum(A[K:])
print(sum)
