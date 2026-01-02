

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    cnt=0
    a=0
    b=0
    A="A"
    B="B"
    ab=0
                
    
    for i in range(N):
        s=input()
        cnt+=s.count("AB")
        if s[0]==B and s[-1]==A:
            ab+=1
        elif s[0]==B:
            b+=1
        elif s[-1]==A:
            a+=1
            
    if a==0 and b==0:
        cnt+=ab-1
        if ab==0:
            cnt+=1
    else:
        cnt+=ab
    ans=cnt+min(a,b)
    print(ans)

main()
