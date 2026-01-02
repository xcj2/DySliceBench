import sys
import numpy as np
input = sys.stdin.readline

 
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def TL(mylist):
    return np.array(mylist).T.tolist()

mylist1 = [list(map(int, input().rstrip().split())) for i in range(3)]
mylist2 = TL(mylist1)

def chech(mylist):
    result = True
    b1 = mylist[0][0] - mylist[0][1]
    c1 = mylist[0][0] - mylist[0][2]
    for i in range(1, 3):
        if (mylist[i][0] -  mylist[i][1]) != b1 or (mylist[i][0] -  mylist[i][2]) != c1:
            result = False
            break
    return result
    
if chech(mylist1) and chech(mylist2):
    print("Yes")
else:
    print("No")