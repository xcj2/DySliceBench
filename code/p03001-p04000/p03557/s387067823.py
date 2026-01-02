import sys
#import math
#import queue
#import copy
import bisect#2分探索

def input():
    return sys.stdin.readline()[:-1]
def inputi():
    return int(input())
def inputl():
    return list(map(int, input().split()))
def printl(li):
    print(*li, sep="\n")
def argsort(s):
    return sorted(range(len(s)), key=lambda k: s[k])

#mod = 10**9+7

N = inputi()
#N, K = inputl()
#L = [int(input()) for i in range(N)]
A = inputl()
B = inputl()
C = inputl()
#S = [inputl() for i in range(H)]
#q = queue.Queue() #q.put(i) #q.get() 
#q = queue.LifoQueue() #q.put(i) #q.get() 

#a= [[0]*3 for i in range(5)] #2次元配列はこう準備、[[0]*3]*5だとだめ
#b=copy.deepcopy(a)  #2次元配列はこうコピーする
#w.sort(key=lambda x:x[1],reverse=True)  #二個目の要素で降順並び替え

#素数リスト
# n = 100
# primes = set(range(2, n+1))
# for i in range(2, int(n**0.5+1)):
#     primes.difference_update(range(i*2, n+1, i))
# primes=list(primes)

#bisect.bisect_left(a, 4)#aはソート済みである必要あり。aの中から最も左の4位置を返す。
#bisect.insort_left(a, 4)#挿入


##TLE
# A.sort(reverse=True)
# B.sort()
# C.sort()
# tot=0
# cut=N
# for a in A:
#     cut=bisect.bisect_right(B[0:cut], a)
#     cut2=N
#     for i in reversed(range(cut,N)):
#         b=B[i]
#         cut2=bisect.bisect_right(C[0:cut2], b)
#         tot+=N-cut2

#right ans
tot=0
A.sort()
C.sort()
for b in B:
    cut1=bisect.bisect_left(A, b)
    cut2=bisect.bisect_right(C, b)
    tot+=cut1*(N-cut2)
print(tot)