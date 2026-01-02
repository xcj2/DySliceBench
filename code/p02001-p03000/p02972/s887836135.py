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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N = _I()
A = LI()

'''
全箱にボールを入れてしまうと、2**N時間かかってしまうので無理
後ろから見たほうが絶対良い
最後の箱には、1であればボールが入るし、、0であればいれない
その次に、その数の約数を大きい方から確認していく
例えば、800が最後だとするとその次は400になる

'''


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

ans = [None for _ in range(N)]
divisor_data = [None for _ in range(N)]
for n in reversed(range(0, N)):
    #  print('n', n)
    if divisor_data[n] == None:
        #  print('none')
        # 約数ではない数字
        if A[n] == 0:
            # ボールは入れない
            ans[n] = 0
        else:
            # ボール入れる
            ans[n] = 1
            divisors = sorted(make_divisors(n+1))
            #  print('divisors', divisors)
            for d in divisors[:-1]:
                if divisor_data[d-1] == None:
                    divisor_data[d-1] = 1
                else:
                    divisor_data[d-1] ^= 1
    else:
        #  print('yakusu')
        # 上の数字の約数
        if divisor_data[n] == A[n]:
            # ボールを入れない
            ans[n] = 0
        else:
            # 玉を追加
            ans[n] = 1
            divisors = sorted(make_divisors(n+1))
            #  print('divisors', divisors)
            for d in divisors[:-1]:
                if divisor_data[d-1] == None:
                    divisor_data[d-1] = 1
                else:
                    divisor_data[d-1] ^= 1
    #  print('div_data', divisor_data)

#  print('ans', ans)
#  print('div_data', divisor_data)
if all(a == 0 for a in ans):
    print(0)
else:
    print(ans.count(1))
    for aidx, a in enumerate(ans):
        if a == 1:
            print(aidx+1, end=' ')


