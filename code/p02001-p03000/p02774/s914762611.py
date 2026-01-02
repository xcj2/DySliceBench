def General_Binary_Increase_Search(L,R,cond,Integer=True,ep=1/(1<<20)):
    """条件式が単調増加であるとき,一般的な二部探索を行う.
    L:解の下限
    R:解の上限
    cond:条件(1変数関数,広義単調減少 or 広義単調減少を満たす)
    Integer:解を整数に制限するか?
    ep:Integer=Falseのとき,解の許容する誤差
    """
    if not(cond(R)):
        return False

    if Integer:
        R+=1
        while R-L>1:
            C=L+(R-L)//2
            if cond(C):
                R=C
            else:
                L=C
        return R
    else:
        while (R-L)>=ep:
            C=L+(R-L)/2
            if cond(C):
                R=C
            else:
                L=C
        return R

def f(R):
    I=0
    S=0
    for a in Pos:
        if I<Negative:
            while a*Neg[I]<=R:
                I+=1
                if I==Negative:
                    break

        S+=I
    return S

def g(R):
    S=0

    I=Positive
    for a in Pos:
        if I>0:
            while a*Pos[I-1]>R:
                I-=1
                if I==0:
                    break
        S+=I
        if a*a<=R:
            S-=1

    J=0
    for b in Neg:
        if J<Negative:
            while b*Neg[-(J+1)]<=R:
                J+=1
                if J==Negative:
                    break
        S+=J
        if b*b<=R:
            S-=1

    return S>>1
#================================================
N,K=map(int,input().split())

A=list(map(int,input().split()))
A.sort()

Pos=[a for a in A if a>0]
Neg=[a for a in A if a<0]

Positive=Zero=Negative=0
for a in A:
    if a>0:
        Positive+=1
    elif a==0:
        Zero+=1
    else:
        Negative+=1

Pos_Count=(Positive*(Positive-1))//2+(Negative*(Negative-1))//2
Neg_Count=Positive*Negative
Zero_Count=(N*(N-1))//2-(Pos_Count+Neg_Count)

H=max(A,key=lambda a:abs(a))
H=H*H+1

if Neg_Count+1<=K<=Neg_Count+Zero_Count: #ゼロ確定
    Ans=0
elif K<=Neg_Count: #負確定
    Ans=General_Binary_Increase_Search(-H,0,lambda x:f(x)>=K)
else: #正確定
    Ans=General_Binary_Increase_Search(0,H,lambda x:g(x)>=K-(Neg_Count+Zero_Count))

print(Ans)