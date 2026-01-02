# In[1]:


N=int(input())
s=[]
for _ in range(N):
    s.append(input())


# In[2]:


def countAB(string):
    cnt=0
    for i in range(len(string)-1):
        if string[i]+string[i+1]=="AB":
            cnt+=1
    return cnt


# In[3]:


def endA(string):
    if string[-1]=="A" and string[0]!="B":
        return 1
    else: return 0
def initB(string):
    if string[0]=="B" and string[-1]!="A":
        return 1
    else: return 0
def endAinitB(string):
    if string[0]=="B" and string[-1]=="A":
        return 1
    else: return 0


# In[4]:


simple_AB=0
Aend=0
Binit=0
eAiB=0
for s_tmp in s:
    simple_AB+=countAB(s_tmp)
    Aend+=endA(s_tmp)
    Binit+=initB(s_tmp)
    eAiB+=endAinitB(s_tmp)
if Aend+Binit>0:
    print(simple_AB+min(Aend, Binit)+eAiB)
elif Aend+Binit==0 and eAiB>0:
    print(simple_AB+eAiB-1)
else: print(simple_AB)