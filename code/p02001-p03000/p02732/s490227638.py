import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(N):
        dd[A[i]]+=1
    
    ans=0
    for k,v in dd.items():
        ans+=(v*(v-1))//2
        
    for i in range(N):
        a=A[i]
        v=dd[A[i]]
        temp=ans
        temp-=(v*(v-1))//2
        temp+=((v-1)*(v-2))//2
        
        print(temp)
    
main()
