

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    from collections import deque
    s=list(input())
    dq=deque(s)
    
    ans=0
    while len(dq)>=2:
        l=dq.popleft()
        r=dq.pop()
        if l==r:
            pass
        elif l=="x":
            ans+=1
            dq.append(r)
        elif r=="x":
            ans+=1
            dq.appendleft(l)
        else:
            print(-1)
            exit()
            
    print(ans)

main()
