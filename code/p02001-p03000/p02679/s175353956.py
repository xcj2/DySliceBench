def modpow(a,n,p):
    if n==0:
        return 1
    x=modpow(a,n//2,p)
    x=(x*x)%p
    if (n%2)==1:
        x=(x*a)%p
    return x%p
def modinv(a,p):
    return modpow(a,p-2,p)
def ggcd(a,b):
    if(b==0):
        return a
    return ggcd(b,a%b)
import math
import fractions
import collections
import itertools
import pprint
N=int(input())
l1=[]
adivb=[]
bis0=0
bdiva=[]
ais0=0
both0=0
p=10**9+7
fish=[list(map(int,input().split())) for _ in range(N)]
fishcomp=[]
d={}
for i in range(N):
    #イメージ的にはa/bを格納していく感じ
    #ai/bi==-bj/ajならダメ
    a=fish[i][0]
    b=fish[i][1]
    g=ggcd(abs(a),abs(b))
    if g!=0:        #ggcdの定義よりa=b=0なら0になりそう(a=0,b!=0ならb,逆もしかり)
        a=a//g
        b=b//g
    #ここらへんで、a,bをそのgcdで割ることによる正規化が完了しているはず
    if b<0:
        a=-a
        b=-b
    #b<0の時に強制的にbを正の値に変換しても影響はない(これを噛ませると後々嬉しい)
    if (a!=0)or(b!=0):
        if d.get(a)==None:
            d[a]={}
            d[a][b]=1
        else:
            if d[a].get(b)==None:
                d[a][b]=1
            else:
                val=d[a].get(b)
                d[a][b]=val+1
        fishcomp.append([a, b])
    else:
        both0=both0+1
#print(d)
#print(fishcomp)
fishcomp=list(map(list,set(map(tuple,fishcomp))))   #二次元配列のset(地味にreferenceがないやつ)
#print(fishcomp)
length=N-both0
sets=[]
#以下ではai/bi==-bj/ajの組みを探している。d[a][b]の個数とd[-b][a]の個数のみ探せば良い
#実はbを正に固定したのがここで生きる。[a b]→[-b a][b,-a]と2つ候補が出るが、
#a>0なら[-b a]に、a<0なら[b,-a]の一つになり、a=0なら[±b 0]だが、これは上で一括して1にまとめているため無問題
#同時にd[a][b]と合わせてダメなのはd[b][-a],d[-b][a]であるが、一方のみ取れば大丈夫
for i in fishcomp:
    a=i[0]
    b=i[1]
    val1=d[a][b]
    #print(a,b,val1)
    if d.get(-b)!=None:
        if d[-b].get(a)!=None:
            val2=d[-b][a]
            sets.append([val1,val2])
            length=length-(val2+val1)
#print(sets,length)
pro=1
for i in sets:
    pro=(pro*(pow(2,i[0],p)+pow(2,i[1],p)-1))%p
#print(pro)
print((pow(2,length,p)*pro-1+both0)%p)