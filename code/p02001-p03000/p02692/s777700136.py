def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A,B,C=MI()
    S=[]
    SS=A+B+C
    for i in range(N):
        s=input()
        S.append(s)
    
    S.append("AB")
    S.append("AB")#適当に入れとけ
    
    ans=[]
    flag=1
    
    if SS==0:
        flag=-1
    elif SS==2:
        for i in range(N):
            s=S[i]
            if s=="AB":
                if A<B:
                    A+=1
                    B-=1
                    ans.append("A")
                elif B<A:
                    A-=1
                    B+=1
                    ans.append("B")
                else:#同数
                    s2=S[i+1]
                    if s2=="AC":
                        A+=1
                        B-=1
                        ans.append("A")
                    else:
                        A-=1
                        B+=1
                        ans.append("B")
                        
                    
            elif s=="AC":
                if A<C:
                    A+=1
                    C-=1
                    ans.append("A")
                elif A>C:
                    A-=1
                    C+=1
                    ans.append("C")
                else:#同数
                    s2=S[i+1]
                    if s2=="AB":
                        A+=1
                        C-=1
                        ans.append("A")
                    else:
                        A-=1
                        C+=1
                        ans.append("C")
                    
            else:#BC
                if C<B:
                    C+=1
                    B-=1
                    ans.append("C")
                elif C>B:
                    C-=1
                    B+=1
                    ans.append("B")
                else:#同数
                    s2=S[i+1]
                    if s2=="AC":
                        C+=1
                        B-=1
                        ans.append("C")
                    else:
                        C-=1
                        B+=1
                        ans.append("B")
                
   
        
                
            if A<0 or B<0 or C<0:
                flag=-1
                break
            #print(i,s,ans[-1])
            #print(A,B,C)
        
    else:
        for i in range(N):
            s=S[i]
            if s=="AB":
                if A<B:
                    A+=1
                    B-=1
                    ans.append("A")
                else:
                    A-=1
                    B+=1
                    ans.append("B")
                
                        
                    
            elif s=="AC":
                if A<C:
                    A+=1
                    C-=1
                    ans.append("A")
                else:
                    A-=1
                    C+=1
                    ans.append("C")
                
                    
            else:#BC
                if C<B:
                    C+=1
                    B-=1
                    ans.append("C")
                else:
                    C-=1
                    B+=1
                    ans.append("B")
                      
            if A<0 or B<0 or C<0:
                flag=-1
                break

                
        
        
    if flag==-1:
        print("No")
        
    else:
        print("Yes")
        for i in range(N):
            print(ans[i])
            
            
        
    
    

main()
