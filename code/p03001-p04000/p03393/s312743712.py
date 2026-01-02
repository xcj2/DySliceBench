import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
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
    if len(x) == 0:
        return []
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
    return "".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

s = list(input())[:-1]

ans = ""

po = [0 for i in range(26)]

if jo(s) == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

if len(s) == 26:
    for i in range(25,-1,-1):
        if i == 25:
            po[ord(s[-1])-97] = 1
            continue
        else:
            if s[i] > s[i+1]:
                po[ord(s[i])-97] = 1
                po[ord(s[i+1])-97] = 1
            else:
                ans = jo(s[:i])
                for j in range(26):
                    if po[j] and ord(s[i])-97 < j:
                        ans += chr(97+j)
                        break
                

                break


else:
    for i in range(len(s)):
        on = ord(s[i])-97
        if po[on] == 0:
            ans += s[i]
            po[on] = 1
    for j in range(26):
        if po[j] == 0:
            ans += chr(97+j)
            break

print(ans)

