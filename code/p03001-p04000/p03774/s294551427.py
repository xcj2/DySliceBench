import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    a=[0]*N
    b=[0]*N
    c=[0]*M
    d=[0]*M
    
    for i in range(N):
        aa,bb=MI()
        a[i]=aa
        b[i]=bb
        
    for i in range(M):
        cc,dd=MI()
        c[i]=cc
        d[i]=dd
        
    def calc(x1,y1,x2,y2):
        return abs(x2-x1)+abs(y2-y1)
    
    def s_calc(x,y):
        temp=10**10
        pos=-1
        for i in range(M):
            l=calc(x,y,c[i],d[i])
            if temp>l:
                temp=l
                pos=i+1
                
        return pos
    
    for i in range(N):
        print(s_calc(a[i],b[i]))
            

main()
