
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    on=0
    L=[]
    cn=0#後ろに置くやつ

    for i in range(N):
        s=input()
        close=0
        openn=0
        for ch in s:
            if ch==")":
                if openn==0:
                    close+=1
                else:
                    openn-=1
            else:
                openn+=1
                
                
        if close==0:
            on+=openn
        elif openn==0:
            cn+=close
        else:
            L.append((close-openn,close,-1*openn))
    L.sort()
    flag=1
    
    #print(on)
    
    for co in L:
        cc=co[1]
        oo=co[2]
        #print(cc,oo)
        on-=cc
        if on<0:
            flag=0
            break
        on-=oo
        
    on-=cn   
    
    if on!=0:
        flag=0
        
    if flag==1:
        print("Yes")
    else:
        print("No")
        
        
    
      
        
    

main()
