import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

h,w,m=MI()
bomb=set()
row=[0]*h
col=[0]*w
for _ in range(m):
    i,j=MI1()
    row[i]+=1
    col[j]+=1
    bomb.add((i,j))
rmx=max(row)
cmx=max(col)
ii=[]
for i in range(h):
    if row[i]==rmx:ii.append(i)
jj=[]
for j in range(w):
    if col[j]==cmx:jj.append(j)
ans=rmx+cmx
for i in ii:
    for j in jj:
        if (i,j) not in bomb:
            print(ans)
            exit()
print(ans-1)
