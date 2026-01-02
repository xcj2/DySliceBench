from collections import defaultdict
import os, sys
if os.environ.get("USER") == "hoge":
    def debug(*args): print(*args, file=sys.stderr)
else:
    def debug(*args): pass
def debug(*args): pass
N=int(input())
A=[int(i) for i in input().split()]
dd=defaultdict(int)
for a in A:
    dd[a]+=1
#print(dd)
B=sorted(A,reverse=True)
ans=0
for x in B:
    debug(A)
    #print(x)
    if dd.get(x,-1)==0:
        continue
    s=len(bin(x))-3
    if x==1<<s:
        t=dd.get(x,-1)
        if t!=-1:
            ans+=t//2
            dd[x]-=(t//2)*2
            #print(ans)
            #print(dd)
    else:
        s+=1
        #print((1<<s)-x)
        t=dd.get((1<<s)-x,-1)
        if t>=1:
            ans+=1
            dd[x]-=1
            dd[(1<<s)-x]-=1
            #print(ans)
            #print(dd)
print(ans)
