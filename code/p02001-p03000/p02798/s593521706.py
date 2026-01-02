import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

UP=(N+1)//2
DOWN=N-UP

ANS=1<<31

def ten(A):
    LEN=len(A)
    MAX=max(A)
    MIN=min(A)

    BIT=[0]*(MAX-MIN+2)# 出現回数をbit indexed treeの形でもっておく.

    def update(v,w):# index vにwを加える
        while v<=MAX-MIN+1:
            BIT[v]+=w
            v+=(v&(-v))# 自分を含む大きなノードへ. たとえばv=3→v=4

    def getvalue(v):# MIN～vの区間の和を求める
        ANS=0
        while v!=0:
            ANS+=BIT[v]
            v-=(v&(-v))# たとえばv=3→v=2へ
        return ANS

    ANS=0        
    for i in range(LEN):# A[0],A[1],...とBITを更新しながら,各A[i]について転倒数を求める.
        bit_ai=A[i]-MIN+1# A[i]がBITの中で何番目か

        ANS+=i# 今まで出現した個数.
        ANS-=getvalue(bit_ai)# 今まで出現した中で,MIN～bit_aiの個数を減らす.
        # bit_ai～MAXの出現個数が転倒数

        update(bit_ai,1)

    return ANS
    

for i in range(1<<N):
    UD=[0,0]
    S0=[]
    S1=[]

    for j in range(N):
        if (1<<j) & i !=0:
            if j%2==0:
                S0.append((A[j],j))
            else:
                S1.append((A[j],j))
            UD[j%2]+=1

        else:
            if (j+1)%2==0:
                S0.append((B[j],j))
            else:
                S1.append((B[j],j))
                
            UD[(j+1)%2]+=1

    if UD[0]==UP and UD[1]==DOWN:
        S0.sort()
        S1.sort()
        #print(UD,S0,S1)

        for i in range(1,N):
            if i%2==0:
                if S0[i//2][0]>=S1[(i-1)//2][0]:
                    True
                else:
                    break
            else:
                if S1[i//2][0]>=S0[(i-1)//2][0]:
                    True
                else:
                    break
        else:
            K=[]
            for i in range(N):
                if i%2==0:
                    K.append(S0[i//2][1])
                else:
                    K.append(S1[i//2][1])

            #print(K)
            #print(ten(K))

            ANS=min(ANS,ten(K))

if ANS==1<<31:
    print(-1)
else:
    print(ANS)
                    
            
                        
            
    
    
