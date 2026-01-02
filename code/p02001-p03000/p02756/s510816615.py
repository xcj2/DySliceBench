

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
from collections import deque


def main():
    mod=10**9+7
    S=deque(input())
    Q=I()
    dir=0#0で手前につける
    
    for _ in range(Q):
        q=list(input().split())
        if q[0]=="1":
            dir+=1
            dir%=2
        else:
            dir2=dir
            if q[1]=="2":
                dir2+=1
                dir2%=2
            if dir2==0:
                S.appendleft(q[2])
            else:
                S.append(q[2])
            
    ans=list(S)
    
    if dir==1:
        ans=ans[::-1]
        
    print(''.join(map(str, ans)))
        

main()
