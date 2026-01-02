A,B,C,D,E,F=map(int,input().split())

def noudo(weight,sugar):
    if sugar is None:return -1000000000
    else:return(sugar*100/weight)
    
def noudosafe(w,s):
    if (noudo(w,s)<=noudo(100+E,E)):return s
    else:return None
    
def eraseNone(i):
    if i is None:return 0
    else: return i
    
dp=[None]*(F+1) #dp[x]はｘｇの砂糖水の中に最大限入っている砂糖の量
dp[0]=0
for i in range(1,F+1):#iグラムの砂糖水
    sug1,sug2,sug3,sug4=[None]*4
    if i>=100*A:
        sug1=dp[i-100*A]
        if sug1 is not None:
            sug1=noudosafe(i,sug1)
    if i>=100*B:
        sug2=dp[i-100*B]
        if sug2 is not None:
            sug2=noudosafe(i,sug2)
    if i>=C:
        sug3base=dp[i-C]
        if sug3base is not None:
            sug3=noudosafe(i,sug3base+C)
    if i>=D:
        sug4base=dp[i-D]
        if sug4base is not None:
            sug4=(noudosafe(i,sug4base+D))
            
    sug=(sug1,sug2,sug3,sug4)
    if all([k is None for k in sug]):
        continue
    else:
        dp[i]=max([eraseNone(k) for k in sug])

ansi=0
anssugar=0
maxnoudo=0
for x,s in enumerate(dp):
    if x==0:continue
    if maxnoudo<noudo(x,s):
        maxnoudo=noudo(x,s)
        ansi=x
        anssugar=s
if anssugar:print(ansi,anssugar)
else: print(100*A,0)