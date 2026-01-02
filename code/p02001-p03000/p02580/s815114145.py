import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())

H,W,m=NM()
import collections
hl=collections.defaultdict(int)
wl=collections.defaultdict(int)
hwl=set()
for i in range(m):
    h,w=NM()
    hl[h]+=1
    wl[w]+=1
    hwl.add((h,w))
mh=0
mw=0
mhl=[]
mwl=[]
for k,v in hl.items():
    if mh<v:
        mh=v
        mhl=[k]
    elif mh==v:
        mhl.append(k)
for k,v in wl.items():
    if mw<v:
        mw=v
        mwl=[k]
    elif mw==v:
        mwl.append(k)
if len(mhl)*len(mwl)>m:
    print(min(m,mh+mw))
else:
    for i in mhl:
        for j in mwl:
            if not (i,j) in hwl:
                print(min(m,mh+mw))
                quit()
    print(mh+mw-1)