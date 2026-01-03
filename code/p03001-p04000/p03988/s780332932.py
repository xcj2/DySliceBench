def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
n=N()
l=L()
l.sort()
def im():
    print("Impossible")
    quit()
def po():
    print("Possible")
    quit()
if l[0]!=(l[-1]+1)//2:
    im()
import collections
c=collections.Counter(l)
if l[-1]%2:
    if c[l[0]]!=2:
        im()
    for i in range(l[0]+1,l[-1]+1):
        if c[i]<2:
            im()
    po()
if c[l[0]]!=1:
    im()
for i in range(l[0]+1,l[-1]+1):
    if c[i]<2:
        im()
po()