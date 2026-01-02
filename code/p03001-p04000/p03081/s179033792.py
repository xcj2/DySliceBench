import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N, Q = LI()
s = input()
TD = []
T, D = [], []
for i in range(Q):
    t,d = LS()
    TD.append([t,d])


#  N, Q = 10**5, 10**5
#  s = ''.join([random.choice(string.ascii_letters) for i in range(N)])
#  TD = []
#  T, D = [], []
#  for i in range(Q):
#      if i % 2 == 0:
#          TD.append(['a','L'])
#          T.append('a')
#          D.append('L')
#      else:
#          TD.append(['b','R'])
#          T.append('b')
#          D.append('R')


# 真ん中から探す
# 幅がなくなるまでやる
lb, ub = -1, N
first_survived_left = None
previous_mid = None
tmp_mid = (lb+ub)//2
while tmp_mid != previous_mid:
    #  print(tmp_mid)
    if lb+ub < 0:
        mid = 0
    else:
        mid = (lb + ub) // 2
    #  print('mid',mid)
    original_mid = mid
    previous_mid = mid
    for td in TD:
        if td[0] == s[mid]:
            if td[1] == "L":
                mid -= 1
            else:
                mid += 1

            if mid == -1:
                lb = original_mid
                if lb+ub<0:
                    tmp_mid = 0
                else:
                    tmp_mid = (lb+ub)//2
                if tmp_mid == previous_mid:
                    # 左に落ちて終わりの場合
                    first_survived_left = original_mid + 1
                break
            if mid == N:
                # 右に落ちてしまった
                ub = original_mid
                if lb+ub<0:
                    tmp_mid = 0
                else:
                    tmp_mid = (lb+ub)//2
                if tmp_mid == previous_mid:
                    first_survived_left = original_mid
                    print(0)
                    exit()
                break
    else:
        #  print('mid',mid)
        # 落ちなかった
        ub = original_mid
        if lb+ub<0:
            tmp_mid = 0
        else:
            tmp_mid = (lb+ub)//2
        if tmp_mid == previous_mid:
            # 左に落ちずに終了
            #  print('finish', original_mid)
            first_survived_left = original_mid
#  print('left', first_survived_left)

lb, ub = -1, N
first_survived_right = N
previous_mid = None
while (lb + ub) // 2 != previous_mid:
    mid = (lb + ub) // 2
    #  print('-', mid)
    original_mid = mid
    previous_mid = mid
    for td in TD:
        if td[0] == s[mid]:
            if td[1] == "L":
                mid -= 1
            else:
                mid += 1

            if mid == -1:
                lb = original_mid
                if (lb+ub) // 2 == previous_mid:
                    # 左に落ちて終わり
                    first_survived_right = original_mid
                    print(0)
                    exit()
                break

            if mid == N:
                ub = original_mid
                if (lb+ub)//2 == previous_mid:
                    # 右に落ちて終わりの場合
                    first_survived_right = original_mid - 1
                break
    else:
        # 落ちなかった
        lb = original_mid
        if (lb+ub)//2 == previous_mid:
            # 右に落ちずに終了
            first_survived_right = original_mid
#  print('right', first_survived_right)

# 1-indexedに直す
#  print(first_survived_left, first_survived_right)
first_survived_right += 1
print(first_survived_right - first_survived_left)
