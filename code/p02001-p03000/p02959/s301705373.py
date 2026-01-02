import sys
import math
from collections import Counter
import itertools
import fractions
import datetime
from decimal import Decimal
#from functools import reduce

# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
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
A=LI()
B=LI()

cnt=0
i = -1
for b in B:
    i+=1
    if A[i] > B[i]:
        A[i]-=B[i]
        cnt+=B[i]
        continue
    else:
        cnt+=A[i]
        B[i]-=A[i]
    if A[i+1] > B[i]:
        A[i+1] -= B[i]
        cnt+=B[i]
    else:
        cnt+=A[i+1]
        A[i+1] = 0
print(cnt)