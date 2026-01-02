import math
import copy
import bisect







def nCast(number):
    if type(number)==str:
        return int(number)
    for idx in range(0,len(number)):
        if type(number[idx])==str:

            number[idx]=int(number[idx])
        else:
            nCast(number[idx])
    return number
    
def inputArr(w):
    l=list()
    for idx in range(0,w):
        l.append(input())
    return l
def inputArr1(w):
    l=list()
    for idx in range(0,w):
        l.append(input().split())
    return l

n=nCast(input().split())
m=nCast(input().split())

def cmp(l1,l2):

    if len(l1)!=len(l2):
        return len(l1)-len(l2)
    for idx in range(len(l1)-1,0,-1):
        if l1[idx]!=l2[idx]:
            return l1[idx]-l2[idx]
    return 0
def func():
    l=list()
    nn=[1,2,3,4,5,6,7,8,9]
    s=set(m)
    mm=[2,5,5,4,5,6,3,7,6]
    d=dict()
    for idx in nn:
        if idx in s:
            if idx==2 and 5 in s:
                continue
            if idx==3 and 5 in s:
                continue
            if idx==2 and 3 in s:
                continue
            if idx==6 and 9 in s:
                continue
            d[nn[idx-1]]=mm[idx-1]
    for idx in range(0,n[0]+1):
        l.append(list())
    for idx in range(1,n[0]+1):
        for idy in d:
            if idx-d[idy]>0:
                tmp=l[idx-d[idy]][:]
                if len(tmp)==0:
                    continue
                tmp.append(idy)
                #tmp.sort(reverse=True)
                if cmp(tmp,l[idx])>0:
                    l[idx]=tmp
            elif idx-d[idy]==0:
                max=0
                for dd in d:
                    if d[dd]==idx and dd>max:
                        max=dd
                if cmp([max],l[idx])>0:
                    l[idx]=[max]

    result=""
    l[-1].sort(reverse=True)
    for idx in range(0,len(l[-1])):
        result=result+str(l[-1][idx])
    return result



print(func()) 

