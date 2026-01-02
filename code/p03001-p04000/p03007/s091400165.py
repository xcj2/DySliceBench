import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    A.sort(reverse=True)
    
    pl=A[0]#負のものはこちらから引いていく
    mi=A[-1]#正のものはこちらから引いていく
    
    ans=[]
    
    for i in range(N-2):
        a=A[i+1]
        if a>=0:
            ans.append([mi,a])
            mi-=a
        else:
            ans.append([pl,a])
            pl-=a
            
    ans.append([pl,mi])
    print(pl-mi)
    for i in range(len(ans)):
        print(' '.join(map(str, ans[i])))
    

main()
