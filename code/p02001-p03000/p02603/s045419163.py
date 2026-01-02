# import sys
# input = sys.stdin.readline

def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))


# ランレングス圧縮
def rle(lst):
    ans = []
    cnt = 1
    ini = lst[0]
    for i in range(1, len(lst)):
        if ini == lst[i]:
            cnt += 1
        else:
            ans.append((ini, cnt))
            cnt = 1
            ini = lst[i]
    ans.append((ini, cnt))
    return ans

n = int(input())
a = lmp()
t = ["d"]
for i in range(1,n):
    if a[i] >= a[i-1]:
        t.append("u")
    else:
        t.append("d")
rt = rle(t)
if rt[-1][0] == "d":
    rt = rt[:-1]
cum = -1
money = 1000
kabu = 0
for i in range(len(rt)):
    if i % 2 == 0:
        cum += rt[i][1]
        kabu = money//a[cum]
        money -= kabu * a[cum]
    else:
        cum += rt[i][1]
        money += kabu * a[cum]
        kabu = 0
print(money)





