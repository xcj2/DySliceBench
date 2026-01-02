S=input()

# グループに分ける
def make_group(S):
    group=[]
    start=0
    search=0
    for i in range(len(S)):
        if S[i]=="L":
            search=1
        if search==1 and S[i]=="R" :
            group.append(S[start:i])
            start=i
            search=0
    group.append(S[start:])
    #print("group",group)
    return group

# 収束するまでの移動回数
# = 'RL'の外側の文字の多いほう
def count_max_chr(s):
    lr=s.split('RL')
    times=max(len(lr[0]),len(lr[1]))
    #print("times, lr",times,lr)
    return times,lr

# RL の両端のRRR,LLLLなどを最終的な配置に振り分ける
# 2**100=even RRRなどの奇数個目は左に、偶数個目は右
def addlr(s,num):
    for i in range(2):
        num[i%2]+=len(s[i%2])//2
        num[(i+1)%2]+=(len(s[i%2])+1)//2
    #print("num",num)
    return num

newgroup=[]
group=make_group(S)
for s in group:
    #print("begin",s)
    subgroup=[0 for _ in range(len(s))]
    times,lr=count_max_chr(s)
    num=[1,1]
    num=addlr(lr,num)
    #print("num(not func)",num)
    subgroup[len(lr[0])]=num[0]
    subgroup[len(lr[0])+1]=num[1]
    #print("subgroup(not func)",subgroup)
    newgroup.append(subgroup)
    #print("newgroup",newgroup)

ans=""
for i in newgroup:
    for j in i:
        ans+=str(j)+" "
print(ans)