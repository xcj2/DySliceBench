import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    X,Y,A,B,C=MI()
    p=LI()
    q=LI()
    r=LI()
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)
    sp=sum(p[:X])
    sq=sum(q[:Y])
    np=X-1
    nq=Y-1
    nr=0
    p.append(10**10)
    q.append(10**10)
    r.append(-1)
    
    
    while True:
        pp=p[np]
        qq=q[nq]
        rr=r[nr]
        if rr>pp and rr>qq:
            if pp>qq:
                sq=sq-qq+rr
                nr+=1
                nq-=1
            else:
                sp=sp-pp+rr
                nr+=1
                np-=1
        elif rr>pp:
            sp=sp-pp+rr
            nr+=1
            np-=1
        elif rr>qq:
            sq=sq-qq+rr
            nr+=1
            nq-=1
        else:
            break
        
    print(sp+sq)
            
            
    
    
    

main()
