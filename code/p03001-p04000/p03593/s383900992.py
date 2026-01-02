import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W=MI()
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(H):
        a=input()
        for j in range(W):
            dd[a[j]]+=1
            
    L=[]
    for k,v in dd.items():
        L.append(v)
    
    four=0
    two=0
    one=0
    
    for aa in L:
        four+=aa//4
        bb=aa%4
        if bb==2 or bb==3:
            two+=1
        if bb==1 or bb==3:
            one+=1
        
    flag=0    
    if H%2==0 and W%2==0:
        if two==0 and one==0:
            flag=1
    elif H%2==0 and W%2!=0:
        if one==0 and two<=(H//2):
            flag=1
    elif H%2!=0 and W%2==0:
        if one==0 and two<=(W//2):
            flag=1
    else:
        if one<=1 and two<=((H+W)//2):
            flag=1
            
    if flag:
        print("Yes")
    else:
        print("No")
        
            
    
        

main()
