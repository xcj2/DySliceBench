def repeted(S):
    for i in range(1,len(S)):
        if S[i]!=S[0]:
            return False
    return True

def repeted_first(S):
    res=1
    i=1
    while i<len(S) and S[i]==S[0]:
        res+=1
        i+=1
    return res

def repeted_last(S):
    res=1
    i=len(S)-2
    while i>=0 and S[i]==S[-1]:
        res+=1
        i-=1
    return res

def calc_t(S):
    res=0
    temp=1
    for i in range(1,len(S)):
        if S[i]==S[i-1]:
            temp+=1 # 連続する同じ文字の数
        else:
            res+=temp//2
            temp=1
    res+=temp//2
    return res # Sの最後まで見た後

S=input()
K=int(input())

if S[0]!=S[-1]:
    ans=calc_t(S)*K

elif repeted(S):
    ans=(len(S)*K)//2

else:
    rf=repeted_first(S)
    rl=repeted_last(S)
    ans=(calc_t(S)-rf//2-rl//2)*K+rf//2+((rf+rl)//2)*(K-1)+rl//2

print(ans)