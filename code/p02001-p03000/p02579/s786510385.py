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
    return " ".join(map(str,x))
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

h,w = m()

c = l()

d = l()

s = [list(input()[:-1]) for i in range(h)]

data = [[-1 for j in range(w)]for i in range(h)]

po = [cl.deque([]) for i in range(h*w // 2 + 1)]

now = 0
po[0] = cl.deque([[c[0]-1,c[1]-1]])
d[0] -= 1
d[1] -= 1
dire = [[1,0],[0,1],[-1,0],[0,-1]]

#data[c[0]-1][c[1]-1] = 0

while True:
    if now >= h*w // 2 + 1:
        break
    if len(po[now]) == 0:
        now += 1
        continue
    else:
        popo = po[now].popleft()
        if data[popo[0]][popo[1]] != -1 and data[popo[0]][popo[1]] < now:
            continue
        else:
            data[popo[0]][popo[1]] = now
            for kkk in dire:
                if (popo[0] + kkk[0] >= 0 and popo[0] + kkk[0] < h) and (popo[1] + kkk[1] >= 0 and popo[1] + kkk[1] < w):
                    if s[popo[0] + kkk[0]][popo[1] + kkk[1]] == "#":
                        continue
                    if data[popo[0] + kkk[0]][popo[1] + kkk[1]] == -1 or data[popo[0] + kkk[0]][popo[1] + kkk[1]] > now:
                        data[popo[0] + kkk[0]][popo[1] + kkk[1]] = now
                        po[now].append([popo[0]+ kkk[0],popo[1] + kkk[1]])

            for i in range(5):
                i -= 2
                if i + popo[0] < 0 or i + popo[0] >= h:
                    continue
                for j in range(5):
                    j -= 2
                    if j + popo[1] < 0 or j + popo[1] >= w:
                        continue
                    elif s[popo[0]+ i][popo[1] + j] == ".":
                        if data[popo[0]+ i][popo[1] + j] > now+1 or data[popo[0]+ i][popo[1] + j] == -1:
                            if now + 1 <= h*w // 2:
                                data[popo[0]+ i][popo[1] + j] = now+1
                                po[now+1].append([popo[0]+ i,popo[1] + j])


print(data[d[0]][d[1]])