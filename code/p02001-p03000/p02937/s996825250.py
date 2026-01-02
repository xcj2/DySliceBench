import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
import fractions
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


s = list(input())

t = list(input())
flag = -1
on = [[-1 for j in range(len(s))] for i in range(26)]

al = [-1 for i in range(26)]
alll = [0 for i in range(26)]
for i in range(len(s)):
    k = ord(s[i]) - 97
    on[k][i] = i
    if al[k] == -1:
        al[k] = i

for i in range(26):
    for j in range(len(s)-2,-1,-1):
        if on[i][j+1] != -1 and on[i][j] == -1:
            on[i][j] = on[i][j+1]
co = 0
ppp = 0
t = cl.deque(t)
while t:
    k = t.popleft()
    kkk = al[ord(k)-97]
    ppp = kkk+1
    if kkk == -1:
        print(kkk)
        exit()
    while t:
        kt = t.popleft()
        if k == kt:
            if kkk == len(s)-1:
                t.appendleft(kt)
                break
            else:
                kk = on[ord(kt)-97][kkk+1] 
                if kkk >= kk:
                    t.appendleft(kt)
                    break
                else:
                    ppp = kk+1
                    kkk = kk
                    k = kt
        else:
            kk = on[ord(kt)-97][kkk]
            if kkk >= kk:
                t.appendleft(kt)
                break
            else:
                ppp = kk+1
                kkk = kk
                k = kt
    if len(t) != 0:
        co += 1

print(len(s)*co + ppp)


