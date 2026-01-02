import sys
input=sys.stdin.readline
from heapq import heappush,heappop

def int_raw():
    return int(input())
 
def ss_raw():
    return input().split()
 
def ints_raw():
    return tuple(map(int, ss_raw()))

def main():
    Q = int(input())
    sb = 0
    lupper = []
    rlower = []
    s = 0
    for _ in range(Q):
        cmds = tuple(map(int,input().split()))
        if cmds[0]==1:
            _,a,b = cmds
            sb+= b
            if len(lupper)== 0 or a<=-lupper[0]:
                heappush(lupper,-a)
                s+=-lupper[0]-a
                if len(lupper)-len(rlower)>=2:
                    heappush(rlower,-heappop(lupper))
            else:
                heappush(rlower,a)
                s+=a+lupper[0]
                if len(rlower)>len(lupper):
                    s+=-lupper[0]-rlower[0]
                    heappush(lupper,-heappop(rlower))  
        else:
            print (-lupper[0], s+sb)
    
main()
