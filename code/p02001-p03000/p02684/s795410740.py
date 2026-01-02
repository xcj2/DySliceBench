import sys
from functools import lru_cache
 
#read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def mp(arg):
  return map(int,arg.split())
n,k=reads()
ls=[]
a=list(reads())#インデックスと場所のさ１ インデックス版の場所のテレポ先
dic={1:0}#keyの場所を何回めに訪れたか
ls=[1]#index回移動した時の場所
loopcount=loopstart=0
for i in range(1,k+1):
  hoge=ls[-1]
  hoge-=1
  if a[hoge] in dic:
    loopcount=i-dic[a[hoge]]
    loopstart=dic[a[hoge]]
    break
  ls.append(a[hoge])
  dic[a[hoge]]=i
else:
  print(ls[-1])
  exit()
k=(k-loopstart)%loopcount
print(ls[k+loopstart])
