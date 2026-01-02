lens=[1 for _ in range(51)]
nump=[1 for _ in range(51)]
for i in range(50):
    lens[i+1]=2*lens[i]+3
    nump[i+1]=2*nump[i]+1
def level(n):
    return max(lvl for lvl,ln in enumerate(lens) if ln<=n)

def calc():
    table={}
    def _calc(l,x):
        if x==0:
            return 0
        if (l,x) in table:
            return table[(l,x)]
        if x==lens[l]:
            res=nump[l]
        elif x<=lens[l-1]:
            res=_calc(l-1,x-1)
        elif x==lens[l-1]+1:
            res=nump[l-1]
        elif x==lens[l-1]+2:
            res=nump[l-1]+1
        else:
            res=nump[l-1]+1+_calc(l-1,x-lens[l-1]-2)
        table[(l,x)]=res
        return res
    return _calc
whole=calc()
print(whole(*map(int,input().split())))