import sys
import math
from collections import Counter
import itertools
#from functools import reduce

# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SR(): return sys.stdin.readline().rstrip()

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_uppercase2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# リストを改行区切りで出力する
p2D = lambda x: print(*x, sep="\n")
p2E = lambda x: print(''.join(x))
p2S = lambda x: print(*x, sep=" ")

# ###########################################

N=II()
W=LI()
mini=9999999

for i in range(1,N):
    s1=0
    s2=0
    for j in range(1,N+1):
        if j<=i:
            s1+=W[j-1]
        else:
            s2+=W[j-1]
    mini = min(mini, abs(s1-s2))
print(mini)