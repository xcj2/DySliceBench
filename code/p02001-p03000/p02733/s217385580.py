import math
import functools
from operator import add

def main():
    h,w,k = tuple([int(t)for t in input().split()])

    s = [[int(i) for i in list(input())] for _ in range(h)]
    
    cusum = [accumelist(s_) for s_ in s]

    candidates = []

    for i in range(1<<(h-1)):
        subcu = divide(cusum,i)
        subs = divide(s,i)

        subcusum = []

        rowsum = []

        for sub_ in subcu:
            subcusum.append(functools.reduce((lambda a,b:list(map(add,a,b))),sub_))

        for sub_ in subs:
            rowsum.append(functools.reduce((lambda a,b:list(map(add,a,b))),sub_))


        cutnum = 0

        temp = [0]*len(subcusum)

        for j in range(w):
            for l in range(len(subcusum)):
                if subcusum[l][j]-temp[l]>k:
                    if rowsum[l][j]>k:
                        cutnum+=10000
                    temp = [x[j-1] for x in subcusum]
                    cutnum+=1
                    break
        
        candidates.append(cutnum+bin(i).count('1'))

    print(min(candidates))
            
def divide(s,i):
    subs = []
    counter = 0
    pos = 0
    while i!= 0:
        counter +=1
        if i%2==1:
            subs.append(s[pos:counter])
            pos = counter
        i >>=1
 
    subs.append(s[pos:])
    return subs

def accumelist(s):
    if s == []:
        return []
    res = [s[0]]
    for i in range(1,len(s)):
        res.append(res[i-1]+s[i])

    return res

def _add_(a,b):
    return map(add,a,b)
    
if __name__ == "__main__":
    main()