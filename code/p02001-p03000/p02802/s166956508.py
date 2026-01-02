def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
jud = [False for i in range(n)]
pen = [0 for i in range(n)]

for j in range(m):
    p,s = ism()
    p = int(p) - 1
    if jud[p] == False:
        if s == 'AC':
            jud[p] = True
        elif s == 'WA':
            pen[p] += 1

ans = jud.count(True)
cpn = 0
for k in range(n):
    if jud[k] == True:
        cpn += pen[k]

print(ans,cpn)