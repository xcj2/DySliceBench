
import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

n=n_in()

base=[]

for _ in range(n):
    s = s_in()

    c = s[0]
    cnt = 1
    ar = []
    for t in range(1,len(s)):
        if s[t-1] == s[t]:
            cnt += 1
        else:
            ar.append((c,cnt))
            c = s[t]
            cnt = 1
    ar.append((c,cnt))

    start = 0
    if ar[0][0] == ")":
        start = 1

    r = 0 # ( の数
    sgn = 1
    for c,cnt in ar[start:]:
        r += sgn*cnt
        sgn *= -1


    res = ()
    if ar[0][0] == ")":
        if r >= 0:
            res = (ar[0][1], r)
        else:
            res = (ar[0][1]-r,0)
    else:
        if r >= 0:
            res = (0, r)
        else:
            res = (-r, 0)

    base.append(res)

i_cnt = 0
j_cnt = 0

base2 = []

for i,j in base:
    i_cnt += i
    j_cnt += j

    if j > 0:
        base2.append((i,-(j-i),j))

if i_cnt != j_cnt:
    print("No")
    exit()

base2.sort()

current = 0


for i,p,j in sorted(filter(lambda x: x[1] <= 0 ,base2)):
    if current < i:
        print("No")
        exit()
    current -= i
    current += j

base3 = []
for i,p,j in filter(lambda x: x[1] > 0 ,base2):
    base3.append((p,i,j))

base3.sort()

for p,i,j in base3:
    if current < i:
        print("No")
        exit()
    current -= i
    current += j
    
print("Yes")
        
