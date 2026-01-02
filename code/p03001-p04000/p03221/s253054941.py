import copy
def a():return input()#s
def ai():return int(input())#a,n or k
def ma():return map(int, input().split())#a,b,c,d or n,k
def ms():return map(str, input().split())#,a,b,c,d
def lma():return list(map(int, input().split()))#x or y
def lms():return list(map(str, input().split()))#x or y

N, M = ma()
PY = [lma() + [i] for i in range(M)]
KY = PY.sort()
ans = []
cnt = [0]*N
for p, y, i in PY: #for p, y, i in enumerate(PY): はできない
    ans.append(["%06d%06d" % (p, cnt[p - 1] + 1), i])
    cnt[p - 1] += 1
ans = sorted(ans, key=lambda x: x[1])
for a,i in ans:
    print(a)