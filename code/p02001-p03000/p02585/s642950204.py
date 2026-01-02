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
    ans = -10**20
    l = len(cir)
    for start in range(l):
        a = 0
        for i in range(num):
            if start+i == l:
                start = -i
            a += cir[start + i]
            ans = max(ans,a)
    return ans

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








