import math

N = int(input())

# d桁の-2進法表記で表現できる最大の数を返す関数。偶数桁目のbitが全て1、奇数桁目のbitが全て0
def max_negative2(d):
    if d == 1:
        return 1
    elif d%2 == 1:
        return int((1-4**(math.ceil(d/2)))/(1-4))
    else:
        return (-2)**(d-1) + int((1-4**(math.ceil(d/2)))/(1-4))

def min_negative2(d):
    if d == 1:
        return 0
    elif d%2 == 1:
        return (-2)**(d-1) + int((-2)*(1-4**(d//2))/(1-4))
    else:
        return int((-2)*(1-4**(d//2))/(1-4))

# 10進数の数値nと桁数dを与えると、nを-2進法表記したときにd桁目が1となるかどうかを返す関数
def top_bit_flag(n,d):
    if n == 0 and d == 1:
        return False
    else:
        return True if min_negative2(d) <= n <= max_negative2(d) else False

# Nの-2進数表記を大きい桁から埋めていく
# -10**9<=N<=10**, min_negative2(31)<10**9<max_negative2(31), min_negative2(32)<-10**9<max_negative2(32)なので、Nは-2進法表記時に最大で32桁
S = ""
n = N
for d in reversed(range(1,33)):
    if top_bit_flag(n,d):
        S += "1"
        n -= (-2)**(d-1)
    else:
        S += "0"

print(int(S))