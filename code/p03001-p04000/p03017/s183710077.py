import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A,B,C,D =MI()
    S=input()
    A-=1
    B-=1
    C-=1
    D-=1
    
    flag=1
    if "##" in S[A:C+1]:
        flag=0
    if "##" in S[B:D+1]:
        flag=0
        
    if C>D:
        if "..." in S[B-1:D+2]:
            pass
        else:
            flag=0
            
    if flag:
        print("Yes")
    else:
        print("No")
        

main()
