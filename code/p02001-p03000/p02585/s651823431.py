import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

def check(cir,num):
    m = len(cir)
    a = sum(cir)
    if num == 0:
        ss = 0
    elif num == 1:
        ss = max(cir)
    else:
        ac = list(accumulate([0]+cir))
        l = 0
        r = 1
        ss = ac[r]-ac[l]
        i = 0
        while 1:
            if r == m:
                l = ac[l+1:r].index(min(ac[l+1:r])) + l+1
                ss = max(ss,ac[r]-ac[l])
                break
            elif i%2==0:
                r = ac[r+1:l+num+1].index(max(ac[r+1:l+num+1])) + r+1
            else:
                l = ac[l+1:r].index(min(ac[l+1:r])) + l+1
            i+=1
            ss = max(ss,ac[r]-ac[l])

        num = m-num
        l = 0
        r = num
        i = 0
        ss = max(ss,a-ac[r]+ac[l])
        while 1:
            if r == m:
                l = ac[l+1:r-num+1].index(max(ac[l+1:r-num+1])) + l+1
                ss = max(ss,a-ac[r]+ac[l])
                break
            elif i%2==0:
                r = ac[r+1:l+m].index(min(ac[r+1:l+m])) + r+1
            else:
                l = ac[l+1:r-num+1].index(max(ac[l+1:r-num+1])) + l+1
            i+=1
            ss = max(ss,a-ac[r]+ac[l])
    return ss


from itertools import accumulate

n,k = readints()
p = [x-1 for x in readints()]
c = readints()

circles = []
used = [0]*n

for i in range(n):
    if not used[i]:
        circles.append([c[i]])
        used[i] = 1
        j = p[i]
        while not used[j]:
            circles[-1].append(c[j])
            used[j] = 1
            j = p[j]

score = -10**20

for cir in circles:
    m = len(cir)
    a = sum(cir)
    if k>m:
        if a>0:
            score = max(score, (k//m)*a + check(cir,k%m), (k//m-1)*a + check(cir,m))
        else:
            score = max(score,check(cir,m))
    else:
        score = max(score,check(cir,k))

print(score)








