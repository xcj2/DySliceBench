import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

h,w,m = readints()

r = [0]*h
c = [0]*w

d = [set() for i in range(h)]
for i in range(m):
    a,b = (x-1 for x in readints())
    r[a] += 1
    c[b] += 1
    d[a].add(b)

mr = max(r)
mc = max(c)
R = [i for i,x in enumerate(r) if x==mr]
C = [i for i,x in enumerate(c) if x==mc]

flag = 1
if len(R)*len(C)>m:
    flag = 0
else:
    for x in R:
        for y in C:
            if y not in d[x]:
                flag = 0
                break

print(max(r)+max(c)-flag)




