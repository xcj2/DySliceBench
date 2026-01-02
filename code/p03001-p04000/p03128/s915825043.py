import queue
from collections import defaultdict
import copy

N,M=map(int,input().split())
A=list(map(int,input().split()))
ma=[2,5,5,4,5,6,3,7,6]
BA=[[0,0] for _ in range(M)] #(必要本数，-1*数字)
for i in range(M):
    BA[i][1]=-1*A[i]
    BA[i][0]=ma[A[i]-1]
    
BA.sort()

#同じ本数使うものを消去
can=[]
ii=0
while ii <len(BA):
    if BA[ii][0] in can:
        BA.pop(ii)
    else:
        can.append(BA[ii][0])
        ii+=1
M=len(BA)#Mの書き換え

diff=[0]*M#数字変更の際に追加で必要な本数
for i in range(M):
    diff[i]=BA[i][0]-BA[0][0]
    BA[i][1]=BA[i][1]*-1#(必要本数，数字)に直しておく

fi=BA[0]###
#BA.sort(key=lambda x: x[1]*-1)#数字の大きいもの順


    
p=[1]*(N+1)
for i in range(N):
    p[i+1]=p[i]*10

#数字のセットL(sort済み)から作れる最大の数値を出力
def set_to_num(L):
    ans=0
    for i in range(len(L)):
        ans+=L[i]*p[i]
    return ans

#2つの配列を合わせる
def make_set(temp,L):
    ori=copy.deepcopy(temp)
    for i in range(len(L)):
        ori[i]=L[i]
    ori.sort()
    return ori
    

#dd用hash
def make_h(L):
    h=0
    for i in range(len(L)):
        h+=p[i]*L[i]
    return h
    
    
ans=-1
Max_dig=N//fi[0]

for d in range(Max_dig):#減らす桁数
    dig=Max_dig-d
    rem=N-fi[0]*dig
    temp=[fi[1]]*dig
    dd = defaultdict(int)
    q=queue.Queue()
    q.put((rem,[]))#残り本数，入れ替える数字
    
    while not q.empty():
        rem2,L=q.get()
        if rem2==0:
            #print(temp,L)
            LLL=make_set(temp,L)
            #print(LLL)
            ans=max(ans,set_to_num(LLL))
        else:
            for i in range(1,M):#変更候補の数字を見ていく.0番は自身のためのぞく
                if rem2>=diff[i]:
                    LL=copy.deepcopy(L)
                    LL.append(BA[i][1])
                    if len(LL)<=len(temp):
                        LL.sort()
                        h=make_h(LL)
                        if dd[h]==0:
                            q.put((rem2-diff[i],LL))
                            dd[h]=1
    if ans!=-1:
        break
        
print(ans)    