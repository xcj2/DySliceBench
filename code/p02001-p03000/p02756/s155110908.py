

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
from collections import deque


def main():
    mod=10**9+7
    S=input()
    
    from collections import deque
    dq=deque()
    
    for c in S:
        dq.appendleft(c)
        
    rev=0
    Q=I()
    for _ in range(Q):
        q=input().split()
        if q[0]=="1":
            rev=(rev+1)%2
        else:
            f=int(q[1])
            c=q[2]
            
            if (rev+f)%2==1:
                dq.append(c)
            else:
                dq.appendleft(c)
                
    ans=[]
    if rev:
        while dq:
            ans.append(dq.popleft())
    else:
        while dq:
            ans.append(dq.pop())
            
    print(''.join(map(str, ans)))
        

        

main()
