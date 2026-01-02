import copy

s=str(input())
t=str(input())
ls=len(s)
lt=len(t)
S=list(s)
T=list(t)
#print(S,T)


def fill(List):
    for j in range(len(List)):
        if List[j]=='?':
            List[j]='a'
    return List


def change1(index):
    global lt

    cS=copy.copy(S)
    cT=copy.copy(T)
    for k in range(index+1,index+lt):
        if cS[k]=='?':
            cS[k]=cT[k-index]
        elif cS[k]==cT[k-index]:
            pass
        else:
            return False,''
            break
    else:
        return True,''.join(fill(cS))

def change2(index):
    global lt

    cS=copy.copy(S)
    cT=copy.copy(T)
    cS[index]=cT[0]
    for k in range(index+1,index+lt):
        if cS[k]=='?':
            cS[k]=cT[k-index]
        elif cS[k]==cT[k-index]:
            pass
        else:
            return False,''
            break
    else:
        return True,''.join(fill(cS))



L=[]
for i in range(ls-lt+1):
    #print(ls-lt)
    if S[i]==T[0]:
        #print('Yes')
        if change1(i)[0]:
            L.append(change1(i)[1])
    elif S[i]=='?':
        if change2(i)[0]:
            L.append(change2(i)[1])
    


if L:
    L.sort()
    print(L[0])
else:
    print('UNRESTORABLE')