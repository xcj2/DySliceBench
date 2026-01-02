def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

def valid(i):
    ar=[]
    if i-1>=0:
        ar.append(i-1)
    ar.append(i)
    if i+1<=9:
        ar.append(i+1)
    return ar

k=int(input())
cur=[1,2,3,4,5,6,7,8,9]
if k<=9:
    print(cur[k-1])
else:
    while(k>len(cur)):
        new_cur=[]
        for i in cur:
            temp=valid(i%10)
            for j in temp:
                new_cur.append(i*10 + j)
        k-=len(cur)
        cur=new_cur.copy()
    print(cur[k-1])

