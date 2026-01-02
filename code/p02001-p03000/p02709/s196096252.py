from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
# from math import gcd,ceil,floor,factorial
# from fractions import gcd
from functools import reduce
from pprint import pprint

def myinput():
    return map(int,input().split())

def mylistinput(n):
    return [ list(myinput()) for _ in range(n) ]

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col,reverse_flag):
    data.sort(key=lambda x:x[col],reverse=reverse_flag)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

def myoutput(ls,space=True):
    if space:
        if len(ls)==0:
            print(" ")
        elif type(ls[0])==str:
            print(" ".join(ls))
        elif type(ls[0])==int:
            print(" ".join(map(str,ls)))
        else:
            print("Output Error")
    else:
        if len(ls)==0:
            print("")
        elif type(ls[0])==str:
            print("".join(ls))
        elif type(ls[0])==int:
            print("".join(map(str,ls)))
        else:
            print("Output Error")

n = int(input())
a = list(myinput())

ls = []
for i in range(n):
    ls.append([ i,a[i] ])
ls = mysort(ls,1,True)
# print(ls)

dp = [ [0]*(n+1) for _ in range(n+1) ]
# dp[i][l]: Aが大きい方からi番目まで決め，左へ移動した個数がl個である時の，スコアの最大値

for i in range(n):
    f = ls[i][0]
    A = ls[i][1]
    for l in range(i+1):
        #
        # 【このi番目を右へ寄せる場合（左へ寄せない場合）】
        # 移動先t
        t = n - i + l - 1
        # スコア
        s = A*abs(t-f)
        # dpテーブルの要素としての更新候補
        dp1 = dp[i][l] + s
        # 既に入っている値より大きければ更新
        if dp1 > dp[i+1][l]:
            dp[i+1][l] = dp1
        #
        # 【このi番目を左へ寄せる場合】
        # 移動先t
        t = l
        # スコア
        s = A*abs(t-f)
        # dpテーブルの要素としての更新候補
        dp2 = dp[i][l] + s
        #
        # 既に入っている値より大きければ更新
        if dp2 > dp[i+1][l+1]:
            dp[i+1][l+1] = dp2
# pprint(dp)

print(max(dp[n]))