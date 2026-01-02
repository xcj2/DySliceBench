import sys
from functools import lru_cache
 
#read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
inf = float('inf')
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def mp(arg):
  return map(int,arg.split())
n,m=reads()
ls=[]
link=[[]for i in range(n)]
for i in range(m):
  a,b=reads()
  a-=1
  b-=1
  link[a].append(b)
  link[b].append(a) 
count=[inf]*n
count[0]=0
#check={i:1 for i in range(n)}
#target=1-1
hoge=[0]
for i in range(n):
    targets=hoge
    hoge=[]
    for target in targets:
        for ele in link[target]:
            if count[ele]==inf:
                count[ele]=target+1
                #link[ele-1].remove(target)
                hoge.append(ele)
    if not hoge:
        break
if inf in count:
    print("No")
    exit()
print("Yes")
for i in count[1:]:
    print(i)