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

s=SR()
atcoder=0
m=0
target=('A','C','G','T')

for i in range(len(s)):
    if s[i] in target:
        atcoder+=1
    else:
        m=max(m,atcoder)
        atcoder=0
print(max(atcoder,m))