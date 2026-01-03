def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
import collections
n = ii()
A = iil()
d = collections.Counter(A)
fst = 0
sec = 0
for k,v in d.items():
    if v == 1:
        continue
    elif v < 4:
        if k > fst:
            sec = fst
            fst = k
        elif k > sec:
            sec = k
    else:
        if k > fst:
            fst = k
            sec = k
        elif k > sec:
            sec = k
print(fst*sec)