def readinput():
    s=input()
    return s

def printTbl(tbl):
    for l in tbl:
        print(l)

def main(s):
    MOD=10**9+7

    Rtbl=[]
    for _ in range(10):
        Rtbl.append([0]*13)
    for i in range(1,10):
        for j in range(13):
            Rtbl[i][j]=(Rtbl[i-1][j]+j)%13
    #printTbl(Rtbl)

    n=len(s)
    p0=0
    q=[]
    for i in range(n):
        if s[i]!='?':
            p0=(p0*10+int(s[i]))%13
            for j in range(len(q)):
                q[j]=(q[j]*10)%13
        else:
            p0=(p0*10)%13
            for j in range(len(q)):
                q[j]=(q[j]*10)%13
            q.append(1)
    #print(p0,q)

    nq=len(q)
    if nq==0:
        if p0==5:
            return 1
        else:
            return 0

    Ptbl=[]
    for _ in range(13):
        Ptbl.append([0]*nq)
    q0=q[0]
    for i in range(10):
        Ptbl[(Rtbl[i][q0]+p0)%13][0]+=1
    for j in range(1,nq):
        qj=q[j]
        for n in range(10):
            for i in range(13):
                if Ptbl[i][j-1]>0:
                    ii=(i+Rtbl[n][qj])%13
                    Ptbl[ii][j]=(Ptbl[ii][j]+Ptbl[i][j-1])%MOD
    #printTbl(Ptbl)
    return Ptbl[5][nq-1]

def main2(s):
    MOD=10**9+7
    dp=[]
    n=len(s)
    for _ in range(13):
        dp.append([0]*(n+1))
    dp[0][0]=1
    for i in range(n):
        c=s[i]
        for j in range(13):
            for k in range(10):
                if c!='?' and c!=str(k):
                   continue
                jj=(j*10+k)%13
                dp[jj][i+1]=(dp[jj][i+1]+dp[j][i])%MOD
    return dp[5][n]

if __name__=='__main__':
    s=readinput()
    ans=main2(s)
    print(ans)
