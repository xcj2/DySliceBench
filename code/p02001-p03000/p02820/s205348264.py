# coding: utf-8
# Your code here!
import copy
N,K=map(int,input().split())
R,S,P=map(int,input().split())
point=score={'r':R,'s':S,'p':P}
T=input()
l=[[]for i in range(K)]
for i in range(N):
  l[i%K].append(T[i])
def get_point(s1,s2):
    num={'r':0,'s':1,'p':2}
    if num[s1]==(num[s2]+1)%3:
        return point[s2]
    else:return 0
def rest(hand):
    if hand=='r':return['s','p']
    elif hand=='s':return['r','p']
    elif hand=='p':return['r','s']
def cal(mini_l):
    size=len(mini_l)
    kind=['r','s','p']
    score={'r':[],'s':[],'p':[]}
    for hand in kind:
        score[hand].append(get_point(mini_l[0],hand))
    for i in range(1,size):
        for hand in kind:
            choice=''
            tmp_score=-1
            for pre_hand in rest(hand):
                if score[pre_hand][i-1]+get_point(mini_l[i],hand)>tmp_score:
                    choice=pre_hand
                    tmp_score=score[pre_hand][i-1]+get_point(mini_l[i],hand)
            score[hand].append(tmp_score)
    tmp_score=-1
    for hand in kind:
        if score[hand][-1]>tmp_score:
            ans=hand
            tmp_score=score[hand][-1]
    return tmp_score
ans=0
for ll in l:
    ans+=cal(ll)
print(ans)        